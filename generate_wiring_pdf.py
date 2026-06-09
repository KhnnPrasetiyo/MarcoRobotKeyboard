"""
Wiring Diagram PDF Generator - NanoKeyboardController
Versi 2: Lebih jelas untuk orang awam
"""

import os

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.platypus import (HRFlowable, PageBreak, Paragraph,
                                SimpleDocTemplate, Spacer, Table, TableStyle)
from reportlab.platypus.flowables import Flowable

OUTPUT_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "Wiring_NanoKeyboardController.pdf"
)

# ─── WARNA ───────────────────────────────────────────────────────────────────
C_BG = colors.HexColor("#0d1117")
C_DARK = colors.HexColor("#1e272e")
C_CARD = colors.HexColor("#2f3542")
C_RED = colors.HexColor("#ff4757")
C_GREEN = colors.HexColor("#2ed573")
C_YELLOW = colors.HexColor("#ffd32a")
C_ORANGE = colors.HexColor("#ffa502")
C_BLUE = colors.HexColor("#3867d6")
C_PURPLE = colors.HexColor("#a55eea")
C_TEAL = colors.HexColor("#00cec9")
C_GRAY = colors.HexColor("#636e72")
C_LIGHT = colors.HexColor("#dfe6e9")
C_WHITE = colors.white
C_BROWN = colors.HexColor("#8B4513")
C_PINK = colors.HexColor("#fd79a8")


# ─── STYLE HELPER ────────────────────────────────────────────────────────────
def S(name, **kw):
    """TODO: add documentation"""
    defaults = dict(fontName="Helvetica", fontSize=9, leading=13, textColor=C_LIGHT)
    defaults.update(kw)
    return ParagraphStyle(name, **defaults)


TITLE = S(
    "T",
    fontName="Helvetica-Bold",
    fontSize=20,
    textColor=C_ORANGE,
    alignment=TA_CENTER,
    spaceAfter=4,
)
H1 = S(
    "H1", fontName="Helvetica-Bold", fontSize=13, textColor=C_ORANGE, spaceBefore=12, spaceAfter=5
)
H2 = S("H2", fontName="Helvetica-Bold", fontSize=10, textColor=C_GREEN, spaceBefore=8, spaceAfter=4)
BODY = S("B", fontSize=9, leading=13, alignment=TA_JUSTIFY, spaceAfter=3)
NOTE = S(
    "N", fontName="Helvetica-Oblique", fontSize=8.5, textColor=C_YELLOW, spaceAfter=3, leftIndent=8
)
WARN = S("W", fontName="Helvetica-Bold", fontSize=9, textColor=C_RED, spaceAfter=3, leftIndent=8)
MONO = S("M", fontName="Courier-Bold", fontSize=8.5, textColor=C_TEAL, spaceAfter=2)
FOOT = S("F", fontName="Helvetica-Oblique", fontSize=7.5, textColor=C_GRAY, alignment=TA_CENTER)


def HR():
    """TODO: add documentation"""
    return HRFlowable(width="100%", thickness=0.8, color=C_GRAY, spaceAfter=6, spaceBefore=2)


def make_table(data, col_widths, accent=C_ORANGE):
    """TODO: add documentation"""
    ts = TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), C_DARK),
            ("TEXTCOLOR", (0, 0), (-1, 0), accent),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 9),
            ("ALIGN", (0, 0), (-1, 0), "CENTER"),
            ("TOPPADDING", (0, 0), (-1, 0), 7),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 7),
            ("BACKGROUND", (0, 1), (-1, -1), C_CARD),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [C_CARD, colors.HexColor("#252d35")]),
            ("TEXTCOLOR", (0, 1), (-1, -1), C_LIGHT),
            ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
            ("FONTSIZE", (0, 1), (-1, -1), 8.5),
            ("ALIGN", (0, 1), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 1), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 1), (-1, -1), 5),
            ("GRID", (0, 0), (-1, -1), 0.5, C_GRAY),
        ]
    )
    t = Table(data, colWidths=col_widths)
    t.setStyle(ts)
    return t


# ═════════════════════════════════════════════════════════════════════════════
# DIAGRAM BLOK UTAMA — Halaman tersendiri, landscape-like, sangat jelas
# ═════════════════════════════════════════════════════════════════════════════
class ClearWiringDiagram(Flowable):
    """
    Diagram blok bersih bergaya komponen fisik yang mudah dipahami orang awam.
    Layout: kolom kiri = komponen, tengah = Arduino Nano, kanan = komponen
    """

    def __init__(self, width=170 * mm, height=230 * mm):
        """TODO: add documentation"""
        super().__init__()
        self._w = float(width)
        self._h = float(height)

    def wrap(self, aW, aH):
        """TODO: add documentation"""
        return self._w, self._h

    def draw(self):
        """TODO: add documentation"""
        c = self.canv
        W, H = self._w, self._h

        # ── Latar belakang ──────────────────────────────────────────────────
        c.setFillColor(C_BG)
        c.roundRect(0, 0, W, H, 8, fill=1, stroke=0)
        c.setStrokeColor(C_GRAY)
        c.setLineWidth(0.6)
        c.roundRect(2, 2, W - 4, H - 4, 8, fill=0, stroke=1)

        # ── Judul dalam diagram ─────────────────────────────────────────────
        c.setFillColor(C_ORANGE)
        c.setFont("Helvetica-Bold", 11)
        c.drawCentredString(W / 2, H - 16, "WIRING DIAGRAM — NANO KEYBOARD CONTROLLER")
        c.setFillColor(C_GRAY)
        c.setFont("Helvetica", 7.5)
        c.drawCentredString(
            W / 2,
            H - 27,
            "● Merah = +5V / Power     ● Hitam/Abu = GND     ● Warna lain = Kabel Sinyal",
        )

        # ────────────────────────────────────────────────────────────────────
        # UTILITAS LOKAL
        # ────────────────────────────────────────────────────────────────────
        def box(x, y, bw, bh, fill=C_DARK, stroke=C_GRAY, radius=4, lw=1.2):
            """TODO: add documentation"""
            c.setFillColor(fill)
            c.setStrokeColor(stroke)
            c.setLineWidth(lw)
            c.roundRect(x, y, bw, bh, radius, fill=1, stroke=1)

        def txt(text, x, y, size=8, color=C_LIGHT, bold=False, center=False):
            """TODO: add documentation"""
            c.setFillColor(color)
            c.setFont("Helvetica-Bold" if bold else "Helvetica", size)
            if center:
                c.drawCentredString(x, y, text)
            else:
                c.drawString(x, y, text)

        def dot(x, y, r=3, color=C_GREEN):
            """TODO: add documentation"""
            c.setFillColor(color)
            c.circle(x, y, r, fill=1, stroke=0)

        def wire(x1, y1, x2, y2, color=C_GREEN, lw=1.5):
            """Kabel dengan routing L-shape (horizontal dulu lalu vertikal)"""
            c.setStrokeColor(color)
            c.setLineWidth(lw)
            c.setDash([])
            c.line(x1, y1, x2, y2)

        def wire_L(x1, y1, x2, y2, color=C_GREEN, lw=1.5, horiz_first=True):
            """Kabel dengan routing L-shape"""
            c.setStrokeColor(color)
            c.setLineWidth(lw)
            c.setDash([])
            if horiz_first:
                c.line(x1, y1, x2, y1)
                c.line(x2, y1, x2, y2)
            else:
                c.line(x1, y1, x1, y2)
                c.line(x1, y2, x2, y2)

        def badge(x, y, bw, bh, num, color=C_ORANGE):
            """Lingkaran nomor pada koneksi"""
            c.setFillColor(color)
            c.circle(x + bw / 2, y + bh / 2, 7, fill=1, stroke=0)
            c.setFillColor(C_BG)
            c.setFont("Helvetica-Bold", 7)
            c.drawCentredString(x + bw / 2, y + bh / 2 - 2.5, str(num))

        def label_pin(x, y, text, color=C_LIGHT, size=7, align="left"):
            """TODO: add documentation"""
            c.setFillColor(color)
            c.setFont("Helvetica-Bold", size)
            if align == "center":
                c.drawCentredString(x, y, text)
            elif align == "right":
                c.drawRightString(x, y, text)
            else:
                c.drawString(x, y, text)

        # ────────────────────────────────────────────────────────────────────
        # LAYOUT DASAR
        # ────────────────────────────────────────────────────────────────────
        # Arduino Nano di tengah
        nano_x = W / 2 - 28
        nano_w = 56
        nano_y = H / 2 - 48
        nano_h = 100

        # Zona kiri (servo + supply)  |  Zona kanan (tombol + LED)
        left_edge = 8
        right_edge = W - 8
        left_comp_right = nano_x - 12  # batas kanan komponen kiri
        right_comp_left = nano_x + nano_w + 12  # batas kiri komponen kanan

        # ────────────────────────────────────────────────────────────────────
        # 1. ARDUINO NANO (tengah)
        # ────────────────────────────────────────────────────────────────────
        box(nano_x, nano_y, nano_w, nano_h, fill=colors.HexColor("#001a0e"), stroke=C_GREEN, lw=2)

        # Header label
        txt(
            "ARDUINO",
            nano_x + nano_w / 2,
            nano_y + nano_h - 10,
            size=7.5,
            color=C_GREEN,
            bold=True,
            center=True,
        )
        txt(
            "NANO V3",
            nano_x + nano_w / 2,
            nano_y + nano_h - 20,
            size=6.5,
            color=C_TEAL,
            bold=False,
            center=True,
        )

        # USB connector symbol
        box(
            nano_x + 12,
            nano_y + 2,
            32,
            10,
            fill=colors.HexColor("#0a2a2a"),
            stroke=C_TEAL,
            radius=2,
            lw=0.8,
        )
        txt("USB → PC", nano_x + nano_w / 2, nano_y + 7, size=5.5, color=C_TEAL, center=True)

        # ── Pin kiri Arduino (D2–D7, GND, 5V) ────────────────────────────
        # Pin kiri: sinyal servo (D2-D7) + power
        left_pins = [
            # (label, y_offset_dari_nano_y, color, pin_name)
            ("D2 LEFT", 82, C_ORANGE, "D2"),
            ("D3 RIGHT", 72, C_ORANGE, "D3"),
            ("D4 UP", 62, C_ORANGE, "D4"),
            ("D5 DOWN", 52, C_ORANGE, "D5"),
            ("D6 SHIFT", 42, C_ORANGE, "D6"),
            ("D7  A", 32, C_ORANGE, "D7"),
            ("GND", 17, C_GRAY, "GND"),
            ("+5V", 7, C_RED, "5V"),
        ]

        for label_text, y_off, col, pin_id in left_pins:
            py = nano_y + y_off
            # Garis pin keluar dari Arduino
            c.setStrokeColor(col)
            c.setLineWidth(1)
            c.line(nano_x, py, nano_x - 6, py)
            dot(nano_x - 6, py, 2, col)
            # Label pin di dalam Arduino
            txt(pin_id, nano_x + 3, py - 3, size=5.5, color=col)

        # ── Pin kanan Arduino (D8-D12, GND) ──────────────────────────────
        right_pins = [
            ("D8 START", 82, C_GREEN, "D8"),
            ("D9 STOP", 72, C_YELLOW, "D9"),
            ("D10 ESTOP", 62, C_RED, "D10"),
            ("D11 LED-S", 48, colors.HexColor("#00b894"), "D11"),
            ("D12 LED-SV", 38, C_BLUE, "D12"),
            ("GND", 23, C_GRAY, "GND"),
        ]

        for label_text, y_off, col, pin_id in right_pins:
            py = nano_y + y_off
            c.setStrokeColor(col)
            c.setLineWidth(1)
            c.line(nano_x + nano_w, py, nano_x + nano_w + 6, py)
            dot(nano_x + nano_w + 6, py, 2, col)
            txt(pin_id, nano_x + nano_w - 18, py - 3, size=5.5, color=col)

        # ────────────────────────────────────────────────────────────────────
        # 2. SUMBER DAYA & IC 7805 (kiri atas)
        # ────────────────────────────────────────────────────────────────────
        # IC 7805
        ic_x = left_edge
        ic_y = H - 85
        ic_w = 68
        ic_h = 42

        box(ic_x, ic_y, ic_w, ic_h, fill=colors.HexColor("#100020"), stroke=C_PURPLE, lw=1.5)
        txt(
            "IC 7805",
            ic_x + ic_w / 2,
            ic_y + ic_h - 10,
            size=8,
            color=C_PURPLE,
            bold=True,
            center=True,
        )
        txt("9-12V  →  5V", ic_x + ic_w / 2, ic_y + ic_h - 22, size=7, color=C_LIGHT, center=True)

        # Gambar kaki IC 7805
        # IN kiri
        c.setStrokeColor(C_RED)
        c.setLineWidth(1.5)
        c.line(ic_x, ic_y + 12, ic_x - 8, ic_y + 12)
        txt("IN", ic_x - 18, ic_y + 9, size=6.5, color=C_RED)
        # GND bawah
        c.setStrokeColor(C_GRAY)
        c.setLineWidth(1.5)
        c.line(ic_x + ic_w / 2, ic_y, ic_x + ic_w / 2, ic_y - 8)
        txt("GND", ic_x + ic_w / 2 - 8, ic_y - 16, size=6.5, color=C_GRAY)
        # OUT kanan
        c.setStrokeColor(C_GREEN)
        c.setLineWidth(1.5)
        c.line(ic_x + ic_w, ic_y + 12, ic_x + ic_w + 8, ic_y + 12)
        txt("OUT", ic_x + ic_w + 10, ic_y + 9, size=6.5, color=C_GREEN)

        # Label IN/OUT kecil dalam box
        txt("IN", ic_x + 6, ic_y + 9, size=5.5, color=C_RED)
        txt("OUT", ic_x + ic_w - 16, ic_y + 9, size=5.5, color=C_GREEN)

        # ADAPTOR / PSU
        psu_x = left_edge
        psu_y = H - 42
        psu_w = 68
        psu_h = 30
        box(psu_x, psu_y, psu_w, psu_h, fill=colors.HexColor("#1a0000"), stroke=C_RED, lw=1.5)
        txt(
            "ADAPTOR DC",
            psu_x + psu_w / 2,
            psu_y + psu_h - 10,
            size=7.5,
            color=C_RED,
            bold=True,
            center=True,
        )
        txt(
            "9V - 12V / 2A+",
            psu_x + psu_w / 2,
            psu_y + psu_h - 20,
            size=6.5,
            color=C_LIGHT,
            center=True,
        )

        # Pin + dan - adaptor
        dot(psu_x + 14, psu_y + 4, 3, C_RED)
        txt("+", psu_x + 18, psu_y + 1, size=8, color=C_RED, bold=True)
        dot(psu_x + 44, psu_y + 4, 3, C_GRAY)
        txt("−", psu_x + 48, psu_y + 1, size=8, color=C_GRAY, bold=True)

        # Kabel dari Adaptor (+) ke SW1 (vertikal naik)
        wire_L(psu_x + 14, psu_y + 4, ic_x, ic_y + 12, C_RED, 1.5, horiz_first=False)

        # SW1 - POWER SWITCH
        sw1_x = left_edge + 80
        sw1_y = H - 55
        sw1_w = 50
        sw1_h = 32
        box(sw1_x, sw1_y, sw1_w, sw1_h, fill=colors.HexColor("#001800"), stroke=C_GREEN, lw=1.5)
        txt(
            "SW 1",
            sw1_x + sw1_w / 2,
            sw1_y + sw1_h - 9,
            size=8,
            color=C_GREEN,
            bold=True,
            center=True,
        )
        txt(
            "POWER ON/OFF",
            sw1_x + sw1_w / 2,
            sw1_y + sw1_h - 19,
            size=6,
            color=C_LIGHT,
            center=True,
        )
        # Simbol saklar kecil
        c.setStrokeColor(C_GREEN)
        c.setLineWidth(1.2)
        c.line(sw1_x + 12, sw1_y + 8, sw1_x + 20, sw1_y + 8)
        c.line(sw1_x + 20, sw1_y + 8, sw1_x + 28, sw1_y + 14)
        c.line(sw1_x + 28, sw1_y + 8, sw1_x + 38, sw1_y + 8)
        dot(sw1_x + 12, sw1_y + 8, 2, C_GREEN)
        dot(sw1_x + 38, sw1_y + 8, 2, C_GREEN)

        # Kabel PSU(+) → SW1 → IC 7805 IN (via kabel merah)
        # PSU + naik ke SW1 kiri
        wire_L(psu_x + 14, psu_y + 4, sw1_x + 12, sw1_y + 8, C_RED, 1.5, horiz_first=True)
        # SW1 kanan → 7805 IN
        wire_L(sw1_x + 38, sw1_y + 8, ic_x - 8, ic_y + 12, C_RED, 1.5, horiz_first=True)

        # GND adaptor ke GND bus
        gnd_bus_y = H - 310
        wire(psu_x + 44, psu_y + 4, psu_x + 44, gnd_bus_y, C_GRAY, 1.2)

        # SW2 - SERVO SWITCH
        sw2_x = sw1_x
        sw2_y = sw1_y - 48
        sw2_w = 50
        sw2_h = 32
        box(sw2_x, sw2_y, sw2_w, sw2_h, fill=colors.HexColor("#00001a"), stroke=C_BLUE, lw=1.5)
        txt(
            "SW 2",
            sw2_x + sw2_w / 2,
            sw2_y + sw2_h - 9,
            size=8,
            color=C_BLUE,
            bold=True,
            center=True,
        )
        txt(
            "SERVO ON/OFF",
            sw2_x + sw2_w / 2,
            sw2_y + sw2_h - 19,
            size=6,
            color=C_LIGHT,
            center=True,
        )
        # Simbol saklar kecil
        c.setStrokeColor(C_BLUE)
        c.setLineWidth(1.2)
        c.line(sw2_x + 12, sw2_y + 8, sw2_x + 20, sw2_y + 8)
        c.line(sw2_x + 20, sw2_y + 8, sw2_x + 28, sw2_y + 14)
        c.line(sw2_x + 28, sw2_y + 8, sw2_x + 38, sw2_y + 8)
        dot(sw2_x + 12, sw2_y + 8, 2, C_BLUE)
        dot(sw2_x + 38, sw2_y + 8, 2, C_BLUE)

        # 7805 OUT → SW2 → rel 5V servo
        wire_L(ic_x + ic_w + 8, ic_y + 12, sw2_x + 38, sw2_y + 8, C_GREEN, 1.5, horiz_first=True)

        # ────────────────────────────────────────────────────────────────────
        # 3. SERVO BLOK (kiri bawah)
        # ────────────────────────────────────────────────────────────────────
        sv_x = left_edge
        sv_y = 38
        sv_w = 130
        sv_h = H - 85 - sv_y - 20

        box(sv_x, sv_y, sv_w, sv_h, fill=colors.HexColor("#1a0d00"), stroke=C_ORANGE, lw=1.5)
        txt(
            "6 SERVO MG90S",
            sv_x + sv_w / 2,
            sv_y + sv_h - 10,
            size=8,
            color=C_ORANGE,
            bold=True,
            center=True,
        )

        servo_defs = [
            ("1. SERVO LEFT", "D2", C_ORANGE),
            ("2. SERVO RIGHT", "D3", colors.HexColor("#ff9f43")),
            ("3. SERVO UP", "D4", colors.HexColor("#f9ca24")),
            ("4. SERVO DOWN", "D5", colors.HexColor("#6ab04c")),
            ("5. SERVO SHIFT", "D6", colors.HexColor("#22a6b3")),
            ("6. SERVO A", "D7", colors.HexColor("#be2edd")),
        ]

        for i, (sname, spin, scol) in enumerate(servo_defs):
            sy = sv_y + sv_h - 26 - i * 22

            # Kotak servo individual
            box(
                sv_x + 5,
                sy - 8,
                sv_w - 10,
                18,
                fill=colors.HexColor("#2d1500"),
                stroke=scol,
                radius=3,
                lw=0.8,
            )

            txt(sname, sv_x + sv_w / 2, sy + 5, size=7, color=scol, bold=True, center=True)

            # 3 titik kabel di ujung kanan servo box
            kabel_x = sv_x + sv_w - 5
            # SIG
            dot(kabel_x, sy + 4, 2.5, scol)
            # VCC
            dot(kabel_x, sy + 0, 2.5, C_RED)
            # GND
            dot(kabel_x, sy - 4, 2.5, C_GRAY)

            txt("SIG", kabel_x - 18, sy + 2, size=5, color=scol)
            txt("VCC", kabel_x - 18, sy - 2, size=5, color=C_RED)
            txt("GND", kabel_x - 18, sy - 6, size=5, color=C_GRAY)

        # Label kabel 3-kawat servo (legend)
        txt("Tiap servo:", sv_x + 6, sv_y + 10, size=6.5, color=C_LIGHT)
        dot(sv_x + 75, sv_y + 10, 3, C_ORANGE)
        txt("Sinyal", sv_x + 80, sv_y + 7, size=6, color=C_ORANGE)
        dot(sv_x + 105, sv_y + 10, 3, C_RED)
        txt("5V", sv_x + 110, sv_y + 7, size=6, color=C_RED)
        dot(sv_x + 120, sv_y + 10, 3, C_GRAY)

        # Kabel dari SIG servo ke pin Arduino (via kabel warna berbeda)
        for i, (sname, spin, scol) in enumerate(servo_defs):
            sy_servo = sv_y + sv_h - 26 - i * 22 + 4
            # Pin nano_y offset
            nano_pin_y = nano_y + 82 - i * 10

            # Kabel dari servo kanan → kabel horizontal → turun/naik ke pin Arduino
            mid_x = sv_x + sv_w + 4 + i * 1.5  # offset sedikit tiap servo biar tidak overlap

            # Kabel sinyal pendek dari ujung servo ke rel sinyal
            relay_x = sv_x + sv_w + 2
            wire(sv_x + sv_w - 5, sy_servo, relay_x + i * 2, sy_servo, scol, 1)

        # Kabel sinyal: blok relay kanan servo → Arduino kiri
        # Buat satu blok konektor saja (bus sinyal)
        bus_x = sv_x + sv_w + 5
        bus_y_top = sv_y + sv_h - 26 + 4
        bus_y_bot = sv_y + sv_h - 26 - 5 * 22 + 4
        c.setStrokeColor(C_ORANGE)
        c.setLineWidth(0.8)
        c.setDash([2, 2])
        c.line(bus_x, bus_y_top + 4, bus_x, bus_y_bot - 4)  # bus vertikal
        c.setDash([])

        # Kabel dari bus ke Arduino
        for i, (sname, spin, scol) in enumerate(servo_defs):
            sy_servo = sv_y + sv_h - 26 - i * 22 + 4
            nano_pin_y = nano_y + 82 - i * 10

            wire(sv_x + sv_w - 5, sy_servo, bus_x, sy_servo, scol, 1)
            c.setStrokeColor(scol)
            c.setLineWidth(1)
            c.setDash([3, 2])
            # Bus ke pin arduino: horizontal dari bus ke arduino kiri
            c.line(bus_x, nano_pin_y, nano_x - 6, nano_pin_y)
            c.setDash([])
            dot(bus_x, nano_pin_y, 2, scol)

        # VCC servo semua → SW2 output
        wire_L(
            sv_x + sv_w - 5, sv_y + sv_h - 26, sw2_x + 12, sw2_y + 8, C_RED, 1.2, horiz_first=False
        )

        # GND servo semua → GND bus
        wire(sv_x + sv_w - 5, sv_y + sv_h - 26 - 4, sv_x + sv_w - 5, gnd_bus_y, C_GRAY, 1.0)

        # ────────────────────────────────────────────────────────────────────
        # 4. TOMBOL (kanan)
        # ────────────────────────────────────────────────────────────────────
        btn_defs = [
            ("BTN  START", "D8", C_GREEN, H - 100),
            ("BTN  STOP", "D9", C_YELLOW, H - 140),
            ("BTN  E-STOP", "D10", C_RED, H - 180),
        ]

        for bname, bpin, bcol, by in btn_defs:
            bx = right_comp_left
            bw = 60
            bh = 28

            box(bx, by - bh / 2, bw, bh, fill=colors.HexColor("#0a1a0a"), stroke=bcol, lw=1.5)
            txt(bname, bx + bw / 2, by + 5, size=7.5, color=bcol, bold=True, center=True)
            txt(f"Kaki 1 → {bpin}", bx + bw / 2, by - 6, size=6, color=C_GRAY, center=True)

            # Gambar simbol tombol
            c.setFillColor(bcol)
            c.circle(bx + bw / 2, by + bh / 2 + 6, 4, fill=1, stroke=0)

            # Titik koneksi kiri tombol (ke Arduino)
            dot(bx, by, 3, bcol)

            # Titik koneksi kanan tombol (ke GND)
            dot(bx + bw, by, 3, C_GRAY)

            # Label kaki
            txt("Pin\nArduino", bx - 28, by - 4, size=5.5, color=bcol)
            txt("GND", bx + bw + 4, by - 4, size=5.5, color=C_GRAY)

            # Pin arduino untuk tombol ini
            pin_offsets = {"D8": 82, "D9": 72, "D10": 62}
            nano_pin_y = nano_y + pin_offsets[bpin]

            # Kabel dari Arduino kanan ke tombol kiri
            mid_x = (nano_x + nano_w + 6 + bx) / 2
            c.setStrokeColor(bcol)
            c.setLineWidth(1.5)
            c.setDash([])
            c.line(nano_x + nano_w + 6, nano_pin_y, bx, by)

            # Kabel GND dari tombol kanan ke bus
            wire_L(bx + bw, by, right_edge - 5, by, C_GRAY, 1, horiz_first=True)

        # ────────────────────────────────────────────────────────────────────
        # 5. LED INDIKATOR (kanan bawah)
        # ────────────────────────────────────────────────────────────────────
        led_defs = [
            ("LED STATUS", "D11", colors.HexColor("#00b894"), H - 225, "Hijau"),
            ("LED SERVO AKTIF", "D12", C_BLUE, H - 265, "Biru"),
        ]

        for lname, lpin, lcol, ly, lcolor_name in led_defs:
            lx = right_comp_left

            # Resistor box
            rx = lx
            box(rx, ly - 8, 28, 16, fill=C_DARK, stroke=C_GRAY, radius=2, lw=0.8)
            txt("330Ω", rx + 14, ly - 3, size=6, color=C_GRAY, center=True)

            # LED body (segitiga simbol)
            led_bx = rx + 34
            c.setFillColor(lcol)
            c.setStrokeColor(lcol)
            c.setLineWidth(0.8)
            path = c.beginPath()
            path.moveTo(led_bx, ly + 7)
            path.lineTo(led_bx + 12, ly)
            path.lineTo(led_bx, ly - 7)
            path.close()
            c.drawPath(path, fill=1, stroke=0)
            c.setStrokeColor(lcol)
            c.line(led_bx + 12, ly + 7, led_bx + 12, ly - 7)

            # Label LED
            box(
                led_bx + 16,
                ly - 12,
                62,
                24,
                fill=colors.HexColor("#000d1a"),
                stroke=lcol,
                radius=3,
                lw=1,
            )
            txt(lname, led_bx + 47, ly + 5, size=7, color=lcol, bold=True, center=True)
            txt(f"● Warna: {lcolor_name}", led_bx + 47, ly - 5, size=6, color=C_GRAY, center=True)

            # Kabel dari Arduino ke resistor
            pin_offsets2 = {"D11": 48, "D12": 38}
            nano_pin_y = nano_y + pin_offsets2[lpin]

            c.setStrokeColor(lcol)
            c.setLineWidth(1.3)
            c.setDash([])
            wire_L(nano_x + nano_w + 6, nano_pin_y, rx, ly, lcol, 1.3, horiz_first=True)

            # Kabel GND dari LED ke bus
            wire(led_bx + 12, ly, right_edge - 5, ly, C_GRAY, 0.9)

        # ────────────────────────────────────────────────────────────────────
        # 6. GND BUS & 5V dari Arduino
        # ────────────────────────────────────────────────────────────────────
        # GND Bus — garis hitam tebal horizontal bawah
        gnd_bus_actual_y = 25
        c.setStrokeColor(C_GRAY)
        c.setLineWidth(3)
        c.setDash([])
        c.line(left_edge + 5, gnd_bus_actual_y, right_edge - 5, gnd_bus_actual_y)
        txt(
            "⏚  GND BUS (Semua GND terhubung di sini)",
            left_edge + 10,
            gnd_bus_actual_y + 5,
            size=6.5,
            color=C_GRAY,
        )

        # Arduino GND ke bus
        wire_L(
            nano_x + nano_w + 6,
            nano_y + 23,
            right_edge - 8,
            nano_y + 23,
            C_GRAY,
            1.2,
            horiz_first=True,
        )
        wire(right_edge - 8, nano_y + 23, right_edge - 8, gnd_bus_actual_y, C_GRAY, 1.2)

        # PSU GND ke bus
        wire(psu_x + 44, psu_y + 4, psu_x + 44, gnd_bus_actual_y, C_GRAY, 1.2)

        # 7805 GND ke bus
        wire(ic_x + ic_w / 2, ic_y, ic_x + ic_w / 2, gnd_bus_actual_y, C_GRAY, 1.2)

        # GND Bus tombol ke bus
        wire(right_edge - 5, H - 100, right_edge - 5, gnd_bus_actual_y, C_GRAY, 1)

        # GND LED ke bus
        wire(right_edge - 5, H - 225, right_edge - 5, H - 100, C_GRAY, 0.9)

        # Kabel 5V dari 7805 ke Arduino 5V pin
        wire_L(ic_x + ic_w + 8, ic_y + 12, nano_x - 6, nano_y + 7, C_GREEN, 1.4, horiz_first=True)

        # ────────────────────────────────────────────────────────────────────
        # 7. LEGENDA WARNA KABEL
        # ────────────────────────────────────────────────────────────────────
        leg_items = [
            (C_RED, "Kabel Merah  = +5V / +12V (Tegangan Positif)"),
            (C_GRAY, "Kabel Hitam  = GND (Ground / Negatif)"),
            (C_ORANGE, "Kabel Warna  = Sinyal Servo (berbeda tiap servo)"),
            (C_GREEN, "Kabel Hijau  = Kabel Sinyal (dari Arduino)"),
        ]

        leg_x = W / 2 - 80
        leg_y = H - 12
        for i, (lc, lt) in enumerate(leg_items):
            lxi = leg_x + i * (W / 4)
            c.setStrokeColor(lc)
            c.setLineWidth(2)
            c.line(lxi, leg_y - 3, lxi + 14, leg_y - 3)
            c.setFillColor(C_LIGHT)
            c.setFont("Helvetica", 5.5)
            if i < 2:
                c.drawString(lxi + 16, leg_y - 6, lt)


# ═════════════════════════════════════════════════════════════════════════════
# BUILD PDF
# ═════════════════════════════════════════════════════════════════════════════
def build_pdf():
    """TODO: add documentation"""
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=14 * mm,
        bottomMargin=14 * mm,
    )

    story = []

    def sp(n=6):
        """TODO: add documentation"""
        story.append(Spacer(1, n))

    # ══════════════════════════════════════════════════════════════════════════
    # HALAMAN 1 — DIAGRAM WIRING UTAMA (full page)
    # ══════════════════════════════════════════════════════════════════════════
    story.append(ClearWiringDiagram(width=174 * mm, height=250 * mm))

    # ══════════════════════════════════════════════════════════════════════════
    # HALAMAN 2 — PANDUAN KONEKSI STEP-BY-STEP
    # ══════════════════════════════════════════════════════════════════════════
    story.append(PageBreak())

    story.append(Paragraph("PANDUAN WIRING — LANGKAH DEMI LANGKAH", TITLE))
    story.append(
        Paragraph(
            "Arduino Nano Keyboard Robot Controller",
            S("sub", fontName="Helvetica", fontSize=10, textColor=C_TEAL, alignment=TA_CENTER),
        )
    )
    sp(4)
    story.append(HR())

    # ── STEP 1: SUMBER DAYA ──────────────────────────────────────────────────
    story.append(Paragraph("STEP 1 — Sambungkan Sumber Daya", H1))
    story.append(
        make_table(
            [
                ["Dari", "Ke", "Warna Kabel", "Keterangan"],
                ["Adaptor DC (+)", "SW1 — Kaki IN", "Merah", "Tegangan masuk ke saklar utama"],
                ["SW1 — Kaki OUT", "IC 7805 — Pin IN", "Merah", "Dari saklar ke regulator 7805"],
                ["IC 7805 — Pin OUT", "Arduino pin 5V", "Merah", "5V stabil ke Arduino"],
                ["IC 7805 — Pin OUT", "SW2 — Kaki IN", "Merah", "5V ke saklar daya servo"],
                ["SW2 — Kaki OUT", "VCC semua Servo", "Merah", "5V ke kabel merah tiap servo"],
                ["Adaptor DC (−)", "GND Bus", "Hitam", "Negatif/Ground dari adaptor"],
                ["IC 7805 — Pin GND", "GND Bus", "Hitam", "GND regulator ke bus GND"],
                ["Arduino GND", "GND Bus", "Hitam", "GND Arduino ke bus GND"],
                ["GND semua Servo", "GND Bus", "Hitam", "GND kabel coklat tiap servo"],
            ],
            [3.8 * cm, 3.8 * cm, 3 * cm, 7.4 * cm],
            accent=C_RED,
        )
    )
    sp(4)
    story.append(
        Paragraph(
            "💡 GND Bus adalah titik sambung semua kabel hitam/ground. Bisa pakai terminal blok, "
            "breadboard, atau sambung langsung menjadi satu titik.",
            NOTE,
        )
    )

    sp(6)
    # ── STEP 2: SERVO ────────────────────────────────────────────────────────
    story.append(Paragraph("STEP 2 — Sambungkan 6 Servo MG90S", H1))
    story.append(
        Paragraph(
            "Setiap servo memiliki <b>3 kabel</b>: Oranye/Kuning = Signal, Merah = +5V, Coklat = GND",
            BODY,
        )
    )
    sp(3)
    story.append(
        make_table(
            [
                ["Servo", "Kabel SIGNAL ke", "Kabel MERAH ke", "Kabel COKLAT ke"],
                ["SERVO 1 — LEFT", "Arduino D2", "SW2 Output / Rel 5V Servo", "GND Bus"],
                ["SERVO 2 — RIGHT", "Arduino D3", "SW2 Output / Rel 5V Servo", "GND Bus"],
                ["SERVO 3 — UP", "Arduino D4", "SW2 Output / Rel 5V Servo", "GND Bus"],
                ["SERVO 4 — DOWN", "Arduino D5", "SW2 Output / Rel 5V Servo", "GND Bus"],
                ["SERVO 5 — SHIFT", "Arduino D6", "SW2 Output / Rel 5V Servo", "GND Bus"],
                ["SERVO 6 — A", "Arduino D7", "SW2 Output / Rel 5V Servo", "GND Bus"],
            ],
            [3.5 * cm, 3 * cm, 6 * cm, 5.5 * cm],
            accent=C_ORANGE,
        )
    )
    sp(4)
    story.append(
        Paragraph(
            "⚠ Kabel VCC (merah) semua servo JANGAN langsung ke pin 5V Arduino — "
            "arus 6 servo bisa merusak Arduino. Harus melalui SW2 dari output IC 7805.",
            WARN,
        )
    )

    sp(6)
    # ── STEP 3: TOMBOL ───────────────────────────────────────────────────────
    story.append(Paragraph("STEP 3 — Sambungkan 3 Tombol (Button Momentary)", H1))
    story.append(
        Paragraph(
            "Firmware menggunakan INPUT_PULLUP internal. Tidak perlu resistor tambahan. "
            "Sambungkan saja <b>satu kaki ke pin Arduino</b>, kaki lainnya ke <b>GND</b>.",
            BODY,
        )
    )
    sp(3)
    story.append(
        make_table(
            [
                ["Tombol", "Warna Tombol", "Kaki 1 → Arduino", "Kaki 2 →", "Fungsi"],
                ["BTN START", "Hijau", "D8", "GND Bus", "Mulai eksekusi pola makro"],
                ["BTN STOP", "Kuning", "D9", "GND Bus", "Hentikan eksekusi secara normal"],
                [
                    "BTN E-STOP",
                    "MERAH",
                    "D10",
                    "GND Bus",
                    "DARURAT: hentikan + servo reset ke atas",
                ],
            ],
            [2.5 * cm, 2.5 * cm, 3 * cm, 2.8 * cm, 7.2 * cm],
            accent=C_GREEN,
        )
    )
    sp(4)
    story.append(
        Paragraph(
            "💡 Tombol E-STOP disarankan menggunakan tombol jamur merah besar (emergency mushroom button) "
            "agar mudah dijangkau saat keadaan darurat.",
            NOTE,
        )
    )

    sp(6)
    # ── STEP 4: LED ──────────────────────────────────────────────────────────
    story.append(Paragraph("STEP 4 — Sambungkan 2 LED Indikator", H1))
    story.append(
        Paragraph(
            "Gunakan resistor 330Ω di antara pin Arduino dan kaki (+) LED untuk membatasi arus.",
            BODY,
        )
    )
    sp(3)
    story.append(
        make_table(
            [
                ["LED", "Warna", "Arduino Pin → Resistor 330Ω → LED (+) → LED (−) →", "Perilaku"],
                [
                    "LED STATUS",
                    "Hijau",
                    "D11 → 330Ω → Anoda(+) → Katoda(−) → GND Bus",
                    "Idle: kedip pelan\nBerjalan: kedip cepat\nDarurat: strobe",
                ],
                [
                    "LED SERVO AKTIF",
                    "Biru",
                    "D12 → 330Ω → Anoda(+) → Katoda(−) → GND Bus",
                    "Menyala: servo sedang bergerak\nMati: servo diam",
                ],
            ],
            [2.5 * cm, 1.8 * cm, 9.7 * cm, 4 * cm],
            accent=colors.HexColor("#00b894"),
        )
    )
    sp(4)
    story.append(
        Paragraph(
            "💡 Kaki panjang LED = Anoda (+), kaki pendek = Katoda (−). "
            "Jika LED tidak menyala, coba balik posisinya.",
            NOTE,
        )
    )

    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # HALAMAN 3 — RINGKASAN CEPAT & CATATAN
    # ══════════════════════════════════════════════════════════════════════════
    story.append(Paragraph("RINGKASAN KONEKSI CEPAT", TITLE))
    sp(4)
    story.append(HR())

    story.append(Paragraph("Semua Pin Arduino Nano yang Digunakan", H1))
    story.append(
        make_table(
            [
                ["Pin Arduino", "Terhubung ke", "Jenis Koneksi", "Warna Kabel"],
                ["D2", "Servo LEFT  — Signal", "Output PWM", "Oranye"],
                ["D3", "Servo RIGHT — Signal", "Output PWM", "Kuning"],
                ["D4", "Servo UP    — Signal", "Output PWM", "Kuning Muda"],
                ["D5", "Servo DOWN  — Signal", "Output PWM", "Hijau Muda"],
                ["D6", "Servo SHIFT — Signal", "Output PWM", "Biru Muda"],
                ["D7", "Servo A     — Signal", "Output PWM", "Ungu"],
                ["D8", "BTN START   — Kaki 1", "Input Pullup", "Hijau"],
                ["D9", "BTN STOP    — Kaki 1", "Input Pullup", "Kuning"],
                ["D10", "BTN E-STOP  — Kaki 1", "Input Pullup", "Merah"],
                ["D11", "LED STATUS  — via 330Ω", "Output Digital", "Hijau Tua"],
                ["D12", "LED SERVO   — via 330Ω", "Output Digital", "Biru"],
                ["5V", "Output IC 7805 (5V regulated)", "Power IN", "Merah"],
                ["GND", "GND Bus (semua ground)", "Ground", "Hitam"],
                ["A0", "TIDAK TERHUBUNG (floating)", "Analog Noise Seed", "—"],
            ],
            [2.5 * cm, 6 * cm, 4 * cm, 5.5 * cm],
        )
    )

    sp(10)
    story.append(Paragraph("Urutan Menyalakan Sistem", H1))
    seq_data = [
        ["Urutan", "Langkah", "Keterangan"],
        ["1", "Pastikan SW2 (Servo) = OFF", "Servo belum dialiri daya"],
        ["2", "Sambungkan kabel USB Arduino ke PC", "Driver CH340 harus sudah terinstall"],
        ["3", "Buka aplikasi, pilih port COM, klik Hubungkan", "Tunggu hingga status 'Terhubung'"],
        ["4", "Upload konfigurasi & profil dari aplikasi", "Kalibrasi sudut servo jika perlu"],
        ["5", "Nyalakan SW1 (Power Utama)", "Adaptor mulai mengaliri daya ke sistem"],
        ["6", "Nyalakan SW2 (Servo)", "Servo siap digerakkan"],
        ["7", "Tekan BTN START atau klik tombol di aplikasi", "Robot mulai berjalan sesuai pola"],
    ]
    story.append(make_table(seq_data, [1.5 * cm, 6.5 * cm, 10 * cm], accent=C_TEAL))

    sp(10)
    # Safety notes
    story.append(Paragraph("Peringatan Keselamatan", H1))
    safety = [
        (
            "🔴 DARURAT",
            C_RED,
            "Selalu pasang BTN E-STOP di tempat yang mudah dijangkau. "
            "Tekan E-STOP jika ada servo yang macet atau bergerak tidak wajar.",
        ),
        (
            "⚡ ARUS",
            C_ORANGE,
            "Gunakan adaptor minimal 2A (rekomendasi 3A). "
            "IC 7805 bisa panas — beri jarak ventilasi atau pasang heatsink kecil.",
        ),
        (
            "🔌 GND",
            C_YELLOW,
            "Semua kabel hitam (GND) WAJIB terhubung ke titik GND Bus yang sama. "
            "GND terputus menyebabkan servo gerak liar atau Arduino restart sendiri.",
        ),
        (
            "💡 DRIVER",
            C_TEAL,
            "Jika port COM tidak muncul di aplikasi, install driver CH340 terlebih dahulu "
            "melalui menu 'Koneksi Serial' di aplikasi → klik 'Pasang Driver Otomatis'.",
        ),
    ]
    for badge, bcol, text in safety:
        row = [
            [
                Paragraph(
                    f"<b>{badge}</b>",
                    S("sb", fontName="Helvetica-Bold", fontSize=9, textColor=bcol, leading=12),
                ),
                Paragraph(text, BODY),
            ]
        ]
        ts = TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), C_CARD),
                ("BOX", (0, 0), (-1, -1), 1.2, bcol),
                ("LEFTPADDING", (0, 0), (0, 0), 8),
                ("LEFTPADDING", (1, 0), (1, 0), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
        t = Table(row, colWidths=[2.8 * cm, 15.2 * cm])
        t.setStyle(ts)
        story.append(t)
        sp(4)

    sp(8)
    story.append(HR())
    story.append(
        Paragraph(
            "Dokumen dibuat otomatis dari firmware.ino & app/models.py — NanoKeyboardController v1.2.0",
            FOOT,
        )
    )

    doc.build(story)
    print(f"[OK] PDF berhasil: {OUTPUT_PATH}")


if __name__ == "__main__":
    build_pdf()
