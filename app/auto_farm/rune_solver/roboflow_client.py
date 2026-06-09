"""HTTP client for Roboflow's serverless YOLO endpoint.

Posts a base64-encoded image and returns raw detections (list of
{x, y, width, height, class, confidence}).
"""

from __future__ import annotations

import base64
import io
import os
from pathlib import Path
from typing import Any

import requests
from PIL import Image

DEFAULT_MODEL_ID = "rune-solver-msvzh-z3rhg/1"
DEFAULT_API_URL = "https://serverless.roboflow.com"


class RoboflowClient:
    """TODO: add documentation"""

    def __init__(
        self,
        model_id: str = DEFAULT_MODEL_ID,
        api_url: str = DEFAULT_API_URL,
        api_key: str | None = None,
        confidence: float = 0.4,
        overlap: float = 0.3,
        timeout: float = 25.0,
    ) -> None:
        """TODO: add documentation"""
        raw_key = api_key or os.environ.get("ROBOFLOW_API_KEY")
        if not raw_key:
            raise ValueError("provide api_key or set $ROBOFLOW_API_KEY")

        # Support multiple API keys separated by commas
        if isinstance(raw_key, str):
            self.api_keys = [k.strip() for k in raw_key.split(",") if k.strip()]
        elif isinstance(raw_key, list):
            self.api_keys = [k.strip() for k in raw_key if isinstance(k, str) and k.strip()]
        else:
            self.api_keys = []

        if not self.api_keys:
            raise ValueError("provide api_key or set $ROBOFLOW_API_KEY")

        self.current_key_idx = 0
        self.api_url = api_url.rstrip("/")
        self.model_id = model_id
        self.confidence = confidence
        self.overlap = overlap
        self.timeout = timeout

    def _encode(self, image: Image.Image | str | Path) -> bytes:
        """TODO: add documentation"""
        if isinstance(image, Image.Image):
            buf = io.BytesIO()
            image.convert("RGB").save(buf, format="PNG")
            return base64.b64encode(buf.getvalue())
        return base64.b64encode(Path(image).read_bytes())

    def infer(self, image: Image.Image | str | Path) -> list[dict[str, Any]]:
        """TODO: add documentation"""
        body = self._encode(image)
        url = f"{self.api_url}/{self.model_id}"

        while self.current_key_idx < len(self.api_keys):
            active_key = self.api_keys[self.current_key_idx]
            params = {
                "api_key": active_key,
                "confidence": self.confidence,
                "overlap": self.overlap,
            }
            try:
                try:
                    resp = requests.post(
                        url,
                        params=params,
                        data=body,
                        headers={"Content-Type": "application/x-www-form-urlencoded"},
                        timeout=self.timeout,
                    )
                except requests.exceptions.SSLError as ssl_err:
                    print(
                        f"[RoboflowClient] SSL Verification failed: {ssl_err}. Retrying with verify=False..."
                    )
                    try:
                        import urllib3
                        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                    except Exception:
                        pass
                    resp = requests.post(
                        url,
                        params=params,
                        data=body,
                        headers={"Content-Type": "application/x-www-form-urlencoded"},
                        timeout=self.timeout,
                        verify=False,
                    )

                # Check for rate limit or quota errors:
                # 429: Too Many Requests
                if resp.status_code == 429:
                    print(
                        f"[RoboflowClient] API Key #{self.current_key_idx + 1} terkena Rate Limit (HTTP 429)."
                    )
                    if self.current_key_idx + 1 < len(self.api_keys):
                        print("[RoboflowClient] Beralih ke API Key berikutnya...")
                        self.current_key_idx += 1
                        continue
                    else:
                        resp.raise_for_status()

                # 403: Forbidden (often returned for limit exceeded / billing)
                elif resp.status_code == 403:
                    try:
                        err_msg = resp.json().get("error", {}).get("message", "").lower()
                    except Exception as e:
                        print("Error occurred")
                        err_msg = ""

                    is_limit = any(
                        term in err_msg
                        for term in ["limit", "quota", "billing", "exceeded", "out of"]
                    )
                    if is_limit:
                        print(
                            f"[RoboflowClient] API Key #{self.current_key_idx + 1} Terkena Limit Kuota (HTTP 403: {err_msg})."
                        )
                        if self.current_key_idx + 1 < len(self.api_keys):
                            print("[RoboflowClient] Beralih ke API Key berikutnya...")
                            self.current_key_idx += 1
                            continue
                        else:
                            resp.raise_for_status()
                    else:
                        resp.raise_for_status()

                else:
                    resp.raise_for_status()

                return resp.json().get("predictions", [])

            except requests.exceptions.HTTPError as http_err:
                if http_err.response is not None and http_err.response.status_code in (429, 403):
                    status = http_err.response.status_code
                    if status == 429:
                        is_limit = True
                    else:
                        try:
                            err_msg = (
                                http_err.response.json().get("error", {}).get("message", "").lower()
                            )
                        except Exception as e:
                            print("Error occurred")
                            err_msg = ""
                        is_limit = any(
                            term in err_msg
                            for term in ["limit", "quota", "billing", "exceeded", "out of"]
                        )

                    if is_limit and self.current_key_idx + 1 < len(self.api_keys):
                        print(
                            f"[RoboflowClient] HTTP {status} (Limit). Beralih ke API Key berikutnya..."
                        )
                        self.current_key_idx += 1
                        continue
                raise
            except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as net_err:
                # Network error: Do NOT switch API key, just raise it so fallback to local ViT happens
                print(
                    f"[RoboflowClient] Koneksi internet bermasalah: {net_err}. Tidak mengganti API Key."
                )
                raise

        # If all keys are exhausted
        raise RuntimeError("Semua API Key Roboflow telah terpakai atau terkena limit.")
