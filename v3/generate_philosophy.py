import re

def create_philosophy_page():
    # Read the base template from about1.html
    with open('about1.html', 'r', encoding='utf-8') as f:
        text = f.read()

    # Find where <main ... > starts
    start_match = re.search(r'<main[^>]*>', text)
    if not start_match:
        print("Could not find <main> tag")
        return
    
    start_idx = start_match.end()
    end_idx = text.find("<!-- ═══════ CTA + FOOTER (shared) ═══════ -->")
    
    head_content = text[:start_match.start()]
    tail_content = text[end_idx:]

    # Now define the new main content for Our Philosophy
    main_html = """<main class="bg-[#FDF8F3] text-[#2B1A12] font-sans antialiased overflow-hidden">

        <!-- ═══════ 1. BRAND MANIFESTO HERO ═══════ -->
        <section class="relative pt-32 pb-20 lg:pt-48 lg:pb-32 px-6">
            <div class="absolute -top-32 -right-32 w-96 h-96 bg-[#F4E6D1] rounded-full blur-[100px] opacity-70"></div>
            
            <div class="container mx-auto max-w-7xl relative z-10">
                <div class="flex flex-col lg:flex-row items-center gap-16 lg:gap-24">
                    <div class="lg:w-1/2">
                        <div class="flex items-center gap-4 mb-8">
                            <div class="h-[1px] w-16 bg-[#C4924A]"></div>
                            <span class="text-[#8C6D4F] uppercase tracking-[0.3em] text-xs font-semibold">Our Manifesto</span>
                        </div>
                        <h1 class="text-5xl md:text-7xl lg:text-8xl font-serif text-[#2B1A12] leading-[1.1] tracking-tight mb-8" style="font-family: 'Playfair Display', serif;">
                            True Beauty is Found in <br>
                            <span class="italic font-light text-[#C4924A]">Balance.</span>
                        </h1>
                        <div class="w-12 h-[1px] bg-[#2B1A12] mb-8"></div>
                        <p class="text-lg md:text-xl text-[#2B1A12]/70 font-light max-w-md leading-relaxed mb-8">
                            We believe that aesthetics should never be loud or disconnected. It must be deliberate, rooted in profound medical science, and intrinsically tied to your internal well-being.
                        </p>
                        <p class="text-sm text-[#2B1A12]/50 font-semibold tracking-widest uppercase">The D'Zen Standard</p>
                    </div>
                    
                    <div class="lg:w-1/2 w-full">
                        <div class="relative max-w-lg mx-auto aspect-[4/5] overflow-hidden rounded-t-[1000px] rounded-b-sm shadow-2xl">
                            <img src="https://images.unsplash.com/photo-1552693673-1bf958298935?q=80&w=1200&auto=format&fit=crop" class="w-full h-full object-cover filter brightness-[0.95]" alt="Holistic Dermatology">
                            <div class="absolute inset-0 border border-white/30 m-4 rounded-t-[1000px] rounded-b-sm"></div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ═══════ 2. THE FOUR BALANCES ═══════ -->
        <section class="py-32 bg-white relative">
            <div class="container mx-auto max-w-6xl px-6">
                <div class="text-center mb-20">
                    <h2 class="text-4xl md:text-5xl font-serif text-[#2B1A12] mb-6" style="font-family: 'Playfair Display', serif;">
                        The Four <span class="italic text-[#C4924A] font-light">Balances</span>
                    </h2>
                    <p class="text-[#2B1A12]/60 font-light max-w-2xl mx-auto leading-relaxed">
                        Our philosophy rests on four foundational pillars. When these elements are in perfect equilibrium, we unlock the most luminous, authentic version of you.
                    </p>
                </div>
                
                <div class="grid md:grid-cols-2 gap-x-16 gap-y-16">
                    <!-- Balance 1 -->
                    <div class="relative group">
                        <div class="absolute -left-6 -top-6 text-8xl font-serif text-[#F4E6D1] opacity-50 z-0 transition-transform duration-700 group-hover:-translate-y-4" style="font-family: 'Playfair Display', serif;">1</div>
                        <div class="relative z-10 pl-6 border-l border-[#C4924A]/30">
                            <h3 class="text-2xl font-serif text-[#2B1A12] mb-4" style="font-family: 'Playfair Display', serif;">Science & Nature</h3>
                            <p class="text-[#2B1A12]/70 font-light leading-relaxed text-sm">
                                We harness the rigorous power of medical dermatology while deeply respecting the body's natural regenerative capabilities. We don't force changes; we bio-stimulate them.
                            </p>
                        </div>
                    </div>
                    <!-- Balance 2 -->
                    <div class="relative group">
                        <div class="absolute -left-6 -top-6 text-8xl font-serif text-[#F4E6D1] opacity-50 z-0 transition-transform duration-700 group-hover:-translate-y-4" style="font-family: 'Playfair Display', serif;">2</div>
                        <div class="relative z-10 pl-6 border-l border-[#C4924A]/30">
                            <h3 class="text-2xl font-serif text-[#2B1A12] mb-4" style="font-family: 'Playfair Display', serif;">Aesthetics & Wellness</h3>
                            <p class="text-[#2B1A12]/70 font-light leading-relaxed text-sm">
                                True skin radiance cannot exist in a biological vacuum. We align advanced external treatments with internal diagnostics (hormones, gut health) for comprehensive harmony.
                            </p>
                        </div>
                    </div>
                    <!-- Balance 3 -->
                    <div class="relative group">
                        <div class="absolute -left-6 -top-6 text-8xl font-serif text-[#F4E6D1] opacity-50 z-0 transition-transform duration-700 group-hover:-translate-y-4" style="font-family: 'Playfair Display', serif;">3</div>
                        <div class="relative z-10 pl-6 border-l border-[#C4924A]/30">
                            <h3 class="text-2xl font-serif text-[#2B1A12] mb-4" style="font-family: 'Playfair Display', serif;">Precision & Artistry</h3>
                            <p class="text-[#2B1A12]/70 font-light leading-relaxed text-sm">
                                Injectables and lasers are powerful tools, but in the hands of our experts, they become instruments of subtle artistry—restoring proportion rather than altering identity.
                            </p>
                        </div>
                    </div>
                    <!-- Balance 4 -->
                    <div class="relative group">
                        <div class="absolute -left-6 -top-6 text-8xl font-serif text-[#F4E6D1] opacity-50 z-0 transition-transform duration-700 group-hover:-translate-y-4" style="font-family: 'Playfair Display', serif;">4</div>
                        <div class="relative z-10 pl-6 border-l border-[#C4924A]/30">
                            <h3 class="text-2xl font-serif text-[#2B1A12] mb-4" style="font-family: 'Playfair Display', serif;">Efficacy & Calm</h3>
                            <p class="text-[#2B1A12]/70 font-light leading-relaxed text-sm">
                                Clinical excellence doesn't have to feel clinical. Every highly-effective protocol is delivered in a sanctuary of sensory calm, reducing cortisol to aid healing.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ═══════ 3. WHY INSIDE-OUT ELEVATION MATTERS ═══════ -->
        <section class="py-32 bg-[#FDF8F3]">
            <div class="container mx-auto max-w-7xl px-6">
                <div class="grid lg:grid-cols-2 gap-16 lg:gap-24 items-center">
                    <div class="order-2 lg:order-1 relative">
                        <div class="aspect-[4/3] overflow-hidden rounded-sm shadow-xl">
                            <img src="https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?q=80&w=1000&auto=format&fit=crop" class="w-full h-full object-cover grayscale-[30%]" alt="Wellness Lifestyle">
                        </div>
                        <div class="absolute -bottom-8 -right-8 w-64 h-64 bg-[#E8C99A] rounded-full blur-[80px] opacity-30 -z-10"></div>
                    </div>
                    
                    <div class="order-1 lg:order-2">
                        <span class="text-[#C4924A] uppercase tracking-[0.2em] text-xs font-semibold mb-6 block">The Cellular Level</span>
                        <h2 class="text-4xl md:text-5xl font-serif text-[#2B1A12] mb-8 leading-tight" style="font-family: 'Playfair Display', serif;">
                            Why Inside-Out <br>Elevation Matters
                        </h2>
                        <div class="space-y-6 text-[#2B1A12]/70 font-light text-sm leading-relaxed">
                            <p>
                                The skin is not just a canvas; it is the largest organ of your body and a direct mirror of your internal health. To treat pigmentation, acne, or aging solely from the surface is to treat the symptom, not the source.
                            </p>
                            <p>
                                Cortisol levels, gut microbiome imbalances, hormonal fluctuations, and cellular inflammation drastically impact skin quality and recovery. By diagnosing and addressing these internal markers, we ensure that our external aesthetic protocols perform optimally.
                            </p>
                            <p class="font-medium italic">
                                "We don't just clear the skin; we restore the environment that allows clear skin to thrive."
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ═══════ 4. WHY ISOLATED TREATMENTS ARE OUTDATED ═══════ -->
        <section class="py-32 bg-[#1A110E] text-white relative overflow-hidden">
            <!-- Subtle glowing orb -->
            <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full h-[600px] bg-[#C4924A] rounded-full blur-[200px] opacity-[0.08] pointer-events-none"></div>
            
            <div class="container mx-auto max-w-5xl px-6 relative z-10 text-center">
                <div class="flex items-center justify-center gap-4 mb-8">
                    <div class="h-[1px] w-12 bg-[#E8C99A]/50"></div>
                    <span class="text-[#E8C99A] uppercase tracking-[0.3em] text-xs font-semibold">A Paradigm Shift</span>
                    <div class="h-[1px] w-12 bg-[#E8C99A]/50"></div>
                </div>
                
                <h2 class="text-4xl md:text-5xl font-serif text-white mb-10 leading-tight" style="font-family: 'Playfair Display', serif;">
                    Why Isolated Treatments <br>Are <span class="italic text-[#E8C99A] font-light">Outdated.</span>
                </h2>
                
                <div class="grid md:grid-cols-2 gap-12 mt-16 text-left border-t border-white/10 pt-16">
                    <div>
                        <h3 class="text-lg font-serif text-[#E8C99A] mb-4" style="font-family: 'Playfair Display', serif;">The Old Model: The "Menu" Approach</h3>
                        <p class="text-white/60 font-light text-sm leading-relaxed">
                            Historically, clinics operated like menus. You walk in, request a specific laser or filler, receive it in isolation, and leave. This fragmented approach ignores facial anatomy as a whole, ignores the skin's biological prep, and leads to disjointed, unnatural results.
                        </p>
                    </div>
                    <div>
                        <h3 class="text-lg font-serif text-[#E8C99A] mb-4" style="font-family: 'Playfair Display', serif;">The D'Zen Model: The Protocol Approach</h3>
                        <p class="text-white/60 font-light text-sm leading-relaxed">
                            We don't do isolated "quick fixes". We curate comprehensive protocols. A single session may seamlessly combine bio-remodeling, laser genesis, and targeted nutrition. We treat the whole face, the whole skin, and the whole person.
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <!-- ═══════ 5. THE D'ZEN INTEGRATED JOURNEY ═══════ -->
        <section class="py-32 bg-white">
            <div class="container mx-auto max-w-7xl px-6">
                <div class="text-center mb-24">
                    <h2 class="text-4xl font-serif text-[#2B1A12] mb-4" style="font-family: 'Playfair Display', serif;">The Integrated Journey</h2>
                    <p class="text-[#2B1A12]/60 font-light text-sm">How we craft your bespoke transformation.</p>
                </div>

                <div class="grid md:grid-cols-4 gap-8 relative">
                    <!-- Connecting Line -->
                    <div class="hidden md:block absolute top-6 left-[10%] right-[10%] h-[1px] bg-[#E8C99A]/40 z-0"></div>

                    <!-- Step 1 -->
                    <div class="relative z-10 text-center">
                        <div class="w-12 h-12 rounded-full bg-[#FDF8F3] border border-[#C4924A] text-[#2B1A12] flex items-center justify-center font-serif text-xl mx-auto mb-6" style="font-family: 'Playfair Display', serif;">1</div>
                        <h3 class="text-sm font-semibold tracking-widest uppercase mb-3 text-[#2B1A12]">Discovery</h3>
                        <p class="text-[#2B1A12]/60 font-light text-xs leading-relaxed max-w-[200px] mx-auto">
                            A deep-dive clinical consultation assessing your aesthetic goals, skin history, and biological baseline.
                        </p>
                    </div>
                    
                    <!-- Step 2 -->
                    <div class="relative z-10 text-center">
                        <div class="w-12 h-12 rounded-full bg-[#FDF8F3] border border-[#C4924A] text-[#2B1A12] flex items-center justify-center font-serif text-xl mx-auto mb-6" style="font-family: 'Playfair Display', serif;">2</div>
                        <h3 class="text-sm font-semibold tracking-widest uppercase mb-3 text-[#2B1A12]">Diagnostics</h3>
                        <p class="text-[#2B1A12]/60 font-light text-xs leading-relaxed max-w-[200px] mx-auto">
                            Advanced skin imaging and optional internal wellness screening to uncover the root causes of skin concerns.
                        </p>
                    </div>

                    <!-- Step 3 -->
                    <div class="relative z-10 text-center">
                        <div class="w-12 h-12 rounded-full bg-[#FDF8F3] border border-[#C4924A] text-[#2B1A12] flex items-center justify-center font-serif text-xl mx-auto mb-6" style="font-family: 'Playfair Display', serif;">3</div>
                        <h3 class="text-sm font-semibold tracking-widest uppercase mb-3 text-[#2B1A12]">Curation</h3>
                        <p class="text-[#2B1A12]/60 font-light text-xs leading-relaxed max-w-[200px] mx-auto">
                            Designing a multi-modal protocol combining in-clinic treatments, medical skincare, and wellness adjustments.
                        </p>
                    </div>

                    <!-- Step 4 -->
                    <div class="relative z-10 text-center">
                        <div class="w-12 h-12 rounded-full bg-[#2B1A12] border border-[#2B1A12] text-[#E8C99A] flex items-center justify-center font-serif text-xl mx-auto mb-6" style="font-family: 'Playfair Display', serif;">4</div>
                        <h3 class="text-sm font-semibold tracking-widest uppercase mb-3 text-[#2B1A12]">Elevation</h3>
                        <p class="text-[#2B1A12]/60 font-light text-xs leading-relaxed max-w-[200px] mx-auto">
                            Execution of the protocol with clinical precision, followed by sustained maintenance for enduring radiance.
                        </p>
                    </div>
                </div>
                
                <div class="mt-24 text-center">
                    <a href="../newthree.html#book" class="inline-flex items-center gap-4 group px-10 py-5 bg-[#2B1A12] text-white hover:bg-[#C4924A] transition-colors duration-500 rounded-sm">
                        <span class="text-xs font-semibold uppercase tracking-widest">Begin Your Journey</span>
                    </a>
                </div>
            </div>
        </section>

    </main>"""

    final_html = head_content + main_html + tail_content
    
    with open('our-philosophy.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

if __name__ == '__main__':
    create_philosophy_page()
    print("Successfully created our-philosophy.html")
