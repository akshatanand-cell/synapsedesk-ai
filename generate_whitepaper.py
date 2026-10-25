import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

def generate_pdf():
    pdf_path = r"C:\Users\KIIT\.gemini\antigravity\scratch\meta-vr-2026\synapsedesk-ai\SynapseDesk_AI_Executive_Whitepaper.pdf"
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    
    # Custom Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=colors.HexColor('#0f172a')
    )
    
    subtitle_style = ParagraphStyle(
        'DocSub',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#0284c7')
    )
    
    h2_style = ParagraphStyle(
        'Heading2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#1e293b'),
        spaceBefore=12,
        spaceAfter=6
    )
    
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#334155')
    )
    
    bullet_style = ParagraphStyle(
        'Bullet',
        parent=body_style,
        leftIndent=15,
        firstLineIndent=-10
    )

    story = []

    # Header
    story.append(Paragraph("SynapseDesk AI — Autonomous Spatial Workspace Protocol", title_style))
    story.append(Paragraph("Executive Whitepaper & Architecture Dossier | Meta VR Start Competition 2026", subtitle_style))
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#0284c7'), spaceAfter=14))

    # Abstract / Overview
    story.append(Paragraph("1. Executive Summary & Vision", h2_style))
    story.append(Paragraph(
        "<b>SynapseDesk AI</b> is an entrant-built, hands-first autonomous spatial cognition workspace built exclusively for Meta Quest 3 and Quest 3S via the official <b>Meta Immersive Web SDK (IWSDK v1.1.0)</b>. Traditional VR productivity solutions force users into standing roomscale reaching and awkward physical keyboard dependencies. SynapseDesk AI re-architects spatial work around human ergonomics: operating strictly within a <b>2-foot seated radius arc (r=0.55m)</b>, requiring <b>zero controllers</b>, and utilizing an autonomous 3D agent (The Synapse Core) that decomposes high-level ambitions into prioritized physical task prisms with real-time force-directed auto-clustering.",
        body_style
    ))
    story.append(Spacer(1, 10))

    # Contest Rule Compliance Matrix
    story.append(Paragraph("2. Official Contest Rule & Evaluation Matrix", h2_style))
    
    table_data = [
        [Paragraph("<b>Criteria / Test</b>", body_style), Paragraph("<b>Meta 2026 Mandate</b>", body_style), Paragraph("<b>SynapseDesk AI Implementation</b>", body_style)],
        [
            Paragraph("<b>Hands-First Test</b>", body_style),
            Paragraph("Fully usable with hands end-to-end. Can someone complete the experience without controllers?", body_style),
            Paragraph("<b>100% Controller-Free.</b> Powered by Meta IWSDK Hand Tracking, PokeInteractable fingertip physics, and OneHandGrabbable 3D pinch mechanics.", body_style)
        ],
        [
            Paragraph("<b>Airplane Seat Test</b>", body_style),
            Paragraph("Seated, stationary use. Limit roomscale. Every interaction within a 2ft radius.", body_style),
            Paragraph("<b>Strict 2ft Radius (r=0.55m).</b> Curved cylindrical cockpit and floating lap plinth keeping all cards within reach without leaning.", body_style)
        ],
        [
            Paragraph("<b>One Bus Stop Test</b>", body_style),
            Paragraph("Fast cold start. Clean pause/resume. Complete moment in <= 10 minutes.", body_style),
            Paragraph("<b>5-Minute Sprint Mode.</b> Instant WebXR streaming via GitHub Pages. Focus timer with procedural Web Audio feedback.", body_style)
        ],
        [
            Paragraph("<b>Originality Test</b>", body_style),
            Paragraph("Core experience is Entrant-built. Thin API wrappers highly discouraged.", body_style),
            Paragraph("<b>Entrant-Authored Engine.</b> Custom semantic decomposition state machine, force-directed spatial relaxation, and Web Audio synthesizer.", body_style)
        ],
        [
            Paragraph("<b>Performance</b>", body_style),
            Paragraph("Minimum 60+ FPS lock on Meta Quest hardware.", body_style),
            Paragraph("<b>60+ FPS Lock.</b> Procedurally batched Three.js r185 primitives + Havok WebAssembly physics. Zero heavy GLTF download latency.", body_style)
        ]
    ]

    t = Table(table_data, colWidths=[110, 190, 230])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f1f5f9')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#0f172a')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
    ]))
    story.append(t)
    story.append(Spacer(1, 14))

    # Architecture & Agentic Intelligence
    story.append(Paragraph("3. Agentic Intelligence & Special Award Qualification ($25,000 Focus)", h2_style))
    story.append(Paragraph(
        "SynapseDesk AI targets the <b>Best Agentic Interaction Prize ($25,000)</b> through three technical pillars:",
        body_style
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph("• <b>Autonomous Semantic Decomposition:</b> Breaks natural language goals into prioritized sub-tasks, estimating cognitive load and time duration.", bullet_style))
    story.append(Paragraph("• <b>Force-Directed Spatial Relaxation:</b> The floating 3D Synapse Core computes repulsion/attraction forces in real-time, arranging cluttered nodes into an optimal 40° field-of-view corridor.", bullet_style))
    story.append(Paragraph("• <b>Cognitive Load Telemetry:</b> A dynamic heuristic evaluates active vs. completed tasks, streaming real-time flow state metrics (Deep Flow, Balanced, Overload Risk) to the user.", bullet_style))
    story.append(Spacer(1, 10))

    # Technical Architecture
    story.append(Paragraph("4. Technical Stack & Platform Implementation", h2_style))
    story.append(Paragraph("• <b>Core Engine:</b> Meta Immersive Web SDK (@iwsdk/core v1.1.0-rc.2)", bullet_style))
    story.append(Paragraph("• <b>3D & Shaders:</b> Three.js (r185 / super-three) with procedural materials", bullet_style))
    story.append(Paragraph("• <b>Physics Engine:</b> Havok Physics compiled to WebAssembly", bullet_style))
    story.append(Paragraph("• <b>Spatial UI:</b> @pmndrs/uikit-horizon & @pmndrs/uikit-lucide (Meta Horizon Dark System)", bullet_style))
    story.append(Paragraph("• <b>Procedural Audio:</b> Pure Web Audio API Synthesizer (pentatonic chimes, zero mp3 delay)", bullet_style))
    story.append(Paragraph("• <b>Continuous Deployment:</b> Automated GitHub Actions -> GitHub Pages (HTTPS WebXR streaming)", bullet_style))
    story.append(Spacer(1, 14))

    # Links
    story.append(Paragraph("5. Verification & Live URLs", h2_style))
    story.append(Paragraph("• <b>Live WebXR Application (Vercel):</b> https://synapsedesk-ai.vercel.app/", body_style))
    story.append(Paragraph("• <b>Mirror Deployment (GitHub Pages):</b> https://akshatanand-cell.github.io/synapsedesk-ai/", body_style))
    story.append(Paragraph("• <b>Public Code Repository:</b> https://github.com/akshatanand-cell/synapsedesk-ai", body_style))
    story.append(Paragraph("• <b>Developer / Entrant:</b> Akshat Anand (Meta VR Start Program Member)", body_style))

    doc.build(story)
    print("PDF generated successfully at:", pdf_path)

if __name__ == '__main__':
    generate_pdf()
