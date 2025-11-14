# ia_cosmos.py
from manim import *
import random

class IACosmos(Scene):
    def construct(self):
        # === CONFIG ===
        self.camera.background_color = "#0a001f"
        quotes = [
            ("El riesgo no es malicia… sino competencia.", "Nick Bostrom"),
            ("La IA debe maximizar preferencias humanas.", "Stuart Russell"),
            ("Estamos invocando al demonio.", "Elon Musk"),
            ("Ética requiere diversidad y transparencia.", "Timnit Gebru"),
            ("La IA codifica poder.", "Kate Crawford"),
            ("La IA podría crear una clase inútil.", "Yuval Noah Harari"),
            ("Podemos hacerla beneficiosa.", "Max Tegmark")
        ]

        # === INTRO: TÍTULO ÉPICO ===
        title = Text("IA: SALVADOR DEL COSMOS", font="Cinzel", gradient=(BLUE, CYAN))
        title.scale(1.8).set_stroke(width=2)
        self.play(Write(title), run_time=2)
        self.play(title.animate.scale(0.7).to_corner(UP), run_time=1)
        self.wait(0.5)

        # === NEBULOSAS Y ESTRELLAS ===
        stars = VGroup(*[Dot(radius=0.03, color=WHITE).move_to(random.uniform(-8,8)*RIGHT + random.uniform(-5,5)*UP) for _ in range(200)])
        nebulae = VGroup()
        for color in [PURPLE, BLUE, GREEN]:
            nebula = Circle(radius=random.uniform(2,4), fill_opacity=0.2, color=color, stroke_width=0)
            nebula.move_to(random.uniform(-7,7)*RIGHT + random.uniform(-4,4)*UP)
            nebulae.add(nebula)
        self.play(FadeIn(stars), FadeIn(nebulae), run_time=2)

        # === PORTAL CENTRAL ===
        portal = Circle(radius=1.5, color=TEAL, fill_opacity=0.8).set_stroke(CYAN, width=6)
        ia_text = Text("IA", font="Cinzel", weight=BOLD).scale(1.5).move_to(portal)
        self.play(Create(portal), Write(ia_text), run_time=1.5)
        self.play(portal.animate.scale(1.3), ia_text.animate.scale(1.2), run_time=1)

        # === 7 MUNDOS NACEN ===
        worlds = VGroup()
        for i, (quote, author) in enumerate(quotes):
            angle = i * (2*PI/7)
            pos = 3.5 * np.array([np.cos(angle), np.sin(angle), 0])
            world = Circle(radius=0.6, color=interpolate_color(BLUE, GREEN, i/7), fill_opacity=0.7)
            world.move_to(pos)
            label = Text(author.split()[-1], font="Cinzel").scale(0.4).move_to(pos)
            worlds.add(world, label)
            self.play(GrowFromCenter(world), FadeIn(label), run_time=0.6)
            self.play(Rotate(world, angle=2*PI, about_point=ORIGIN), run_time=0.8)

        self.play(FadeOut(nebulae), run_time=1)

        # === CONEXIONES ÉTICAS ===
        lines = VGroup()
        for w1 in worlds[::2]:
            for w2 in worlds[1::2]:
                if random.random() > 0.6:
                    line = DashedLine(w1.get_center(), w2.get_center(), color=CYAN, stroke_opacity=0.6)
                    lines.add(line)
        self.play(Create(lines), run_time=1.5)

        # === FINAL: MENSAJE + CALL TO ACTION ===
        final = VGroup(
            Text("7 MUNDOS CREADOS", font="Cinzel").scale(1.2),
            Text("CON ÉTICA HUMANA", font="Cinzel").scale(1),
            Text("Hecho en 1 tarde. ¿Y con modelos reales?", font="Cinzel").scale(0.7),
            Text("@xai @elonmusk @grok", font="Cinzel", color=YELLOW).scale(0.8)
        ).arrange(DOWN, buff=0.4).to_edge(DOWN)
        self.play(FadeIn(final), run_time=2)
        self.wait(2)

        # === OUTRO ===
        self.play(FadeOut(VGroup(*self.mobjects)), run_time=1.5)