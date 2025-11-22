// Game State
// Tracing helper (defined in tracing.js). If absent, provide no-op.
const traceEvent = window.traceEvent || function(){};
const gameState = {
    currentNode: 'start',
    collaborationScore: 0,
    relationships: {
        izack: 0,
        aria: 0,
        zara: 0
    },
    choices: []
};

// Story Nodes
const storyNodes = {
    start: {
        text: `
            <p><span class="polly-comment">*Caw!* Alright, new student. Let me guess - you're nervous, excited, and probably wondering if that portal sickness will ever wear off. Spoiler: it won't for another hour. You're welcome for that information.</span></p>

            <p>You stand at the edge of Avalon Academy, watching the impossible spiral spire twist upward into clouds that shimmer with leyline energy. The World Tree's branches arc overhead, and you can <em>feel</em> the convergence of magical currents thrumming through the air.</p>

            <p>A large raven lands on the crystalline gate before you, fixing you with one knowing eye.</p>

            <p><span class="polly-comment">"Welcome to Avalon, where boundaries come to die and collaborative magic is somehow <em>not</em> an oxymoron. I'm Polly. Yes, like the bird. No, the irony is not lost on me. I'll be your narrator, occasional advisor, and the only honest voice you'll hear today."</span></p>

            <p>The raven - Polly - gestures with one wing toward the academy entrance.</p>

            <p><span class="polly-comment">"Izack Thorne himself is waiting to meet the new arrivals. Fair warning: he's brilliant, kind, and will absolutely try to convince you that listening to magical currents is more important than controlling them. He's not wrong, but don't tell him I said that."</span></p>
        `,
        choices: [
            {
                text: "Approach respectfully and introduce yourself properly",
                next: 'polite_intro',
                effects: { collaboration: 1, izack: 1 }
            },
            {
                text: "Ask Polly more questions about what to expect",
                next: 'ask_polly',
                effects: { collaboration: 0, zara: 1 }
            },
            {
                text: "Walk past confidently - you've read about Avalon and know what you're doing",
                next: 'confident_intro',
                effects: { collaboration: -1, aria: 1 }
            }
        ]
    },

    polite_intro: {
        text: `
            <p>You walk through the crystalline gate, feeling the leyline energy wash over you like warm water. Izack Thorne stands in the courtyard - tall, dark-haired, with eyes that seem to see through dimensions.</p>

            <p>"Welcome," he says warmly. "I'm Izack. You must be our newest student. How are you feeling after the portal crossing?"</p>

            <p><span class="polly-comment">*Perched on his shoulder* "Oh good, we got a polite one. Those are always fun to watch when they realize magic here doesn't care about your manners."</span></p>

            <p>Izack shoots Polly a look. "What Polly means is that magic responds to intention and collaboration, not formality. But courtesy is always appreciated."</p>

            <p>He gestures toward the academy. "Your first lesson begins shortly. We'll be exploring the nature of magical boundaries - specifically, how they can be <em>bridged</em> rather than broken."</p>
        `,
        choices: [
            {
                text: "Express excitement about learning collaborative techniques",
                next: 'first_lesson_collab',
                effects: { collaboration: 2, izack: 2 }
            },
            {
                text: "Ask if you'll learn individual magic too - you want to be self-sufficient",
                next: 'first_lesson_mixed',
                effects: { collaboration: 0, aria: 1 }
            }
        ]
    },

    ask_polly: {
        text: `
            <p><span class="polly-comment">"Smart. Ask the raven who's been here since the beginning. I like you already."</span></p>

            <p>Polly hops closer, her feathers catching the leyline light.</p>

            <p><span class="polly-comment">"Here's what you need to know: Avalon is <em>alive</em>. Not metaphorically - Izack literally created a sentient dimensional realm that grows from the World Tree. The magic here works through collaboration, which means your success depends on how well you listen to the currents, your fellow students, and yes, even the cranky raven."</span></p>

            <p>She tilts her head.</p>

            <p><span class="polly-comment">"Izack will teach you to <em>feel</em> magic rather than force it. Aria - his wife, brilliant politician - will teach you precision and boundaries. Zara, their first student, will probably befriend you because she's annoyingly nice. And I'll keep you honest."</span></p>

            <p>Just then, a young woman with hybrid features - pointed ears, striking eyes - approaches with a warm smile.</p>

            <p>"Hi! You must be new. I'm Zara. Polly giving you the full orientation?"</p>
        `,
        choices: [
            {
                text: "Thank Polly and ask Zara what her experience has been like",
                next: 'zara_friendship',
                effects: { collaboration: 1, zara: 2 }
            },
            {
                text: "Ask Zara about the different magical traditions taught here",
                next: 'first_lesson_mixed',
                effects: { collaboration: 1, aria: 1 }
            }
        ]
    },

    confident_intro: {
        text: `
            <p><span class="polly-comment">*Caw!* "Oh, we have a confident one. This should be entertaining."</span></p>

            <p>You stride through the gate with purpose. You've read about Avalon, studied dimensional theory, and you're ready to prove yourself.</p>

            <p>A woman with sharp eyes and elegant bearing steps into your path. Her presence radiates controlled power - this is someone who knows exactly where every boundary lies.</p>

            <p>"Aria Ravencrest," she introduces herself. "Co-founder, boundary specialist, and the person who makes sure enthusiastic students don't accidentally collapse dimensional barriers."</p>

            <p><span class="polly-comment">"That's Izack's wife. She's the reason Avalon hasn't imploded from all the experimental magic. Show some respect."</span></p>

            <p>Aria's expression softens slightly. "Confidence is good. Overconfidence in dimensional magic is how you end up scattered across three realities. Let me ask you something: what do you think is more important - controlling magic, or understanding it?"</p>
        `,
        choices: [
            {
                text: "Controlling it - power without control is dangerous",
                next: 'aria_control',
                effects: { collaboration: -1, aria: 2 }
            },
            {
                text: "Understanding it - you can't work with something you don't comprehend",
                next: 'aria_understanding',
                effects: { collaboration: 2, aria: 1, izack: 1 }
            },
            {
                text: "Both equally - they inform each other",
                next: 'first_lesson_mixed',
                effects: { collaboration: 1, aria: 2 }
            }
        ]
    },

    zara_friendship: {
        text: `
            <p>Zara's face lights up. "It's been incredible! I was the first student here - came from a hybrid bloodline that didn't fit anywhere else. Avalon was the first place that celebrated what I am instead of asking me to choose."</p>

            <p><span class="polly-comment">"She's not exaggerating. Zara's the bridge between traditions. Also, she'll probably want to study with you, so prepare for that."</span></p>

            <p>Zara laughs. "Polly's right. I love working with other students. Magic here is so much stronger when we combine our approaches. My hybrid heritage lets me see connections others miss."</p>

            <p>She gestures toward a crystalline building that pulses with soft light. "Come on, first lesson's about to start. Izack's teaching today - dimensional resonance and collaborative casting."</p>

            <p>As you walk together, you notice leylines glowing beneath the courtyard stones, converging toward the central spire.</p>
        `,
        choices: [
            {
                text: "Ask Zara to partner with you during the lesson",
                next: 'first_lesson_collab',
                effects: { collaboration: 2, zara: 2, izack: 1 }
            },
            {
                text: "Thank her but say you'd like to try solo first to assess your abilities",
                next: 'first_lesson_solo',
                effects: { collaboration: -1, zara: -1 }
            }
        ]
    },

    aria_control: {
        text: `
            <p>Aria nods thoughtfully. "A practical answer. Control <em>is</em> important - I've spent years mastering boundary magic precisely because uncontrolled dimensional rifts are catastrophic."</p>

            <p><span class="polly-comment">"But...?"</span></p>

            <p>"But," Aria continues, "control without understanding is brittle. It breaks under pressure. Izack taught me that magic isn't about domination - it's about partnership."</p>

            <p>She places a hand on your shoulder. "You have the discipline for power. Let me teach you the wisdom to use it well. Come - your first lesson awaits."</p>

            <p><span class="polly-comment">"Translation: Aria likes you but thinks you're going to learn the hard way. I've seen this before. It's educational."</span></p>
        `,
        choices: [
            {
                text: "Accept Aria's guidance and keep an open mind",
                next: 'first_lesson_mixed',
                effects: { collaboration: 1, aria: 2 }
            },
            {
                text: "Respectfully maintain that control should come first, understanding second",
                next: 'first_lesson_solo',
                effects: { collaboration: -1, aria: 1 }
            }
        ]
    },

    aria_understanding: {
        text: `
            <p>Aria's expression shifts to genuine warmth. "Exactly. You can force magic to obey, but it will fight you every step. Understand it, and it becomes a willing partner."</p>

            <p><span class="polly-comment">"Congratulations, you passed Aria's test. She and Izack are going to love you."</span></p>

            <p>Aria smiles. "Polly's not wrong. That's the philosophy at Avalon's core. Magic is alive - it has currents, rhythms, preferences. Learning to <em>listen</em> to those is more powerful than any control technique."</p>

            <p>She guides you toward the academy. "Izack's teaching the first lesson today. You'll practice dimensional resonance - feeling the boundaries between realities and learning to work <em>with</em> them, not against them."</p>

            <p><span class="polly-comment">"Fair warning: this is where things get weird. Dimensional magic feels like falling while standing still. Just go with it."</span></p>
        `,
        choices: [
            {
                text: "Express excitement and ask to learn as much as possible",
                next: 'first_lesson_collab',
                effects: { collaboration: 2, aria: 2, izack: 1 }
            }
        ]
    },

    first_lesson_collab: {
        text: `
            <p>The lesson chamber is breathtaking. Crystalline walls pulse with leyline energy, and dimensional boundaries shimmer visibly in the air like heat waves made of starlight.</p>

            <p>Izack stands at the center, surrounded by five other students. "Welcome. Today we're learning to <em>feel</em> dimensional boundaries. Not to break them, but to understand their nature."</p>

            <p>He gestures, and the air ripples. "Reach out - not with your hands, but with your awareness. What does the boundary feel like?"</p>

            <p>You close your eyes and extend your senses. The boundary feels like... a membrane. Flexible. Almost musical.</p>

            <p><span class="polly-comment">"Good. Now here's the fun part - Izack wants you to work together to create a harmonic resonance. Multiple mages, one unified frequency."</span></p>

            <p>Izack nods. "Exactly. Zara, would you demonstrate with our newest student?"</p>

            <p>Zara takes your hand. "Just match my breathing. Let our intentions align."</p>

            <p>As you breathe together, something incredible happens - your magical senses merge. You can feel the boundary through both perspectives, and it's infinitely clearer.</p>
        `,
        choices: [
            {
                text: "Deepen the connection and try to include the other students",
                next: 'breakthrough_collab',
                effects: { collaboration: 3, izack: 3, zara: 2 }
            },
            {
                text: "Maintain the connection with Zara and perfect it",
                next: 'stable_collab',
                effects: { collaboration: 2, zara: 2 }
            },
            {
                text: "Pull back slightly - the merging feels overwhelming",
                next: 'crisis_setup',
                effects: { collaboration: 0, zara: -1 }
            }
        ]
    },

    first_lesson_mixed: {
        text: `
            <p>The lesson chamber glows with leyline energy. Izack begins the demonstration while Aria observes from the side, her sharp eyes missing nothing.</p>

            <p>"Dimensional magic," Izack explains, "requires both sensitivity and precision. Feel the currents, but understand the structures."</p>

            <p><span class="polly-comment">"Translation: Izack teaches you to listen, Aria teaches you not to die. It's a good system."</span></p>

            <p>Izack has you practice sensing boundaries while Aria guides your technique. It's a balance - intuition meets discipline.</p>

            <p>Aria steps forward. "Now, try to create a small portal. Just a viewing window between here and the courtyard. Focus your intention, but stay aware of the boundary's natural resistance."</p>

            <p>You concentrate, feeling the dimensional membrane. With effort, a small shimmer appears in the air.</p>

            <p><span class="polly-comment">"Not bad. A little shaky, but you're not bleeding from any orifices, so that's a win."</span></p>
        `,
        choices: [
            {
                text: "Ask if you can try collaborating with another student to stabilize it",
                next: 'stable_collab',
                effects: { collaboration: 2, izack: 2 }
            },
            {
                text: "Push yourself to perfect it solo - you want to prove your capability",
                next: 'first_lesson_solo',
                effects: { collaboration: -1, aria: 1 }
            }
        ]
    },

    first_lesson_solo: {
        text: `
            <p>You step forward, determined to show what you can do on your own. Izack watches with interest, while Aria's expression is carefully neutral.</p>

            <p><span class="polly-comment">"Oh boy. Here we go. I've seen this movie before."</span></p>

            <p>You focus entirely on your own power, reaching for the dimensional boundary. The membrane resists, but you push harder, forcing your will against it.</p>

            <p>The portal opens - larger than intended. Energy crackles at its edges.</p>

            <p>Aria's voice cuts through. "Stabilize it. You're pulling too much unfiltered dimensional energy."</p>

            <p><span class="polly-comment">"What she means is: you're about to turn yourself into a dimensional anchovy if you don't ease off."</span></p>

            <p>Panic flickers through you as the portal destabilizes further. Through the opening, you glimpse fractured realities.</p>
        `,
        choices: [
            {
                text: "Swallow your pride and call for help from the other students",
                next: 'crisis_collab_rescue',
                effects: { collaboration: 2, izack: 1, zara: 2 }
            },
            {
                text: "Trust Aria's instruction and try to stabilize it using her technique",
                next: 'crisis_aria_rescue',
                effects: { collaboration: 0, aria: 3 }
            },
            {
                text: "Pour more power into it - if you can open it, you can control it",
                next: 'crisis_disaster',
                effects: { collaboration: -2, izack: -1, aria: -1 }
            }
        ]
    },

    breakthrough_collab: {
        text: `
            <p>You reach out with your awareness, inviting the other students into the resonance. One by one, they join - five minds, five hearts, one unified frequency.</p>

            <p><span class="polly-comment">"Oh. Oh, this is... actually, I'm speechless. That never happens. Caw."</span></p>

            <p>The dimensional boundary doesn't just become visible - it <em>sings</em>. You can feel its nature, its preferences, the way it wants to flex and flow. Together, your group creates a perfect harmonic resonance.</p>

            <p>Izack's eyes shine with unshed tears. "This is exactly what Avalon was built for. You just demonstrated the Third Thread - collaborative magic that transcends individual limitations."</p>

            <p>Aria approaches, clearly moved. "In my years of dimensional work, I've never seen students achieve this level of connection on their first day."</p>

            <p>Zara squeezes your hand, grinning. "We did it!"</p>

            <p><span class="polly-comment">"Alright, don't let it go to your heads. But yes, this was... impressive. Even for Avalon."</span></p>
        `,
        choices: [
            {
                text: "Thank everyone and express how amazing the collaboration felt",
                next: 'ending_collaborative_master',
                effects: { collaboration: 3, izack: 3, aria: 2, zara: 3 }
            },
            {
                text: "Ask if there are opportunities to explore more of Avalon's realms",
                next: 'field_expedition_offer',
                effects: { collaboration: 2, izack: 2 }
            }
        ]
    },

    stable_collab: {
        text: `
            <p>You and Zara maintain the connection, refining it. The boundary becomes crystal clear between your merged awareness.</p>

            <p>Izack nods approvingly. "Beautiful work. This is partnership magic - two becoming greater than the sum of their parts."</p>

            <p><span class="polly-comment">"Solid performance. Not flashy, but that's not always bad. You're learning the right lessons."</span></p>

            <p>Aria steps forward. "Now let's test your understanding. Can you identify the weak points in the boundary? Every dimensional membrane has natural stress points."</p>

            <p>With Zara's help, you scan the shimmering barrier. There - three points where the boundary thins naturally.</p>

            <p>"Exactly," Aria confirms. "Those are potential portal sites. Understanding the boundary's nature lets you work <em>with</em> it instead of forcing it."</p>

            <p>The lesson continues successfully. You've demonstrated both collaborative skill and practical understanding.</p>
        `,
        choices: [
            {
                text: "Ask if you can study more about the Third Thread and collaborative magic",
                next: 'ending_collaborative_scholar',
                effects: { collaboration: 2, izack: 2, zara: 2 }
            },
            {
                text: "Ask Aria about advanced boundary techniques",
                next: 'ending_balanced_mage',
                effects: { collaboration: 1, aria: 3, izack: 1 }
            },
            {
                text: "Ask about field expeditions to explore Avalon's different biomes",
                next: 'field_expedition_offer',
                effects: { collaboration: 1, izack: 1, aria: 1 }
            }
        ]
    },

    crisis_setup: {
        text: `
            <p>You pull back from the merged awareness, suddenly overwhelmed. The sensation of your consciousness blending with Zara's was too much, too fast.</p>

            <p><span class="polly-comment">"Okay, that's fair. It is pretty intense the first time."</span></p>

            <p>But as you withdraw, something goes wrong. The collaborative resonance destabilizes, and the dimensional boundary you were examining begins to crack.</p>

            <p>Zara gasps. "The harmonics are collapsing!"</p>

            <p>Aria's voice cuts through the rising panic. "Everyone, step back. Izack-"</p>

            <p>Izack is already moving, reaching for the fracturing boundary, but you can see the strain on his face. The crack is spreading faster than he can repair it alone.</p>

            <p><span class="polly-comment">"Right. So this is a teachable moment about why we don't panic-quit collaborative spells. Your move, student."</span></p>
        `,
        choices: [
            {
                text: "Rejoin the collaborative effort to help stabilize it",
                next: 'crisis_collab_rescue',
                effects: { collaboration: 2, izack: 1, zara: 1 }
            },
            {
                text: "Stay back and let the teachers handle it - you don't want to make it worse",
                next: 'crisis_passive',
                effects: { collaboration: -1, izack: -1 }
            }
        ]
    },

    crisis_collab_rescue: {
        text: `
            <p>You push past your fear and reach out again - not just to Zara, but to everyone. "Together! Like before!"</p>

            <p>Zara grabs your hand immediately. The other students join. Izack's eyes widen as he feels the collaborative resonance snap into place.</p>

            <p>"That's it," he breathes. "Channel it through me - I'll direct the repair."</p>

            <p>Six students and one master mage, working as one. The fractured boundary responds to your unified intention, the cracks sealing like wounds knitting together.</p>

            <p><span class="polly-comment">"Now THIS is what I'm talking about! Crisis brings out the best collaborative magic. Well done!"</span></p>

            <p>The boundary stabilizes, then settles into a perfect, shimmering membrane. The danger passes.</p>

            <p>Aria exhales. "Impressive crisis management. You recognized that individual strength wasn't enough and chose collaboration instead."</p>

            <p>Izack smiles, clearly proud. "This is exactly why Avalon exists. You just demonstrated its core principle under pressure."</p>
        `,
        choices: [
            {
                text: "Apologize for causing the crisis, but express gratitude for learning the lesson",
                next: 'ending_collaborative_scholar',
                effects: { collaboration: 3, izack: 3, zara: 2 }
            }
        ]
    },

    crisis_aria_rescue: {
        text: `
            <p>You focus entirely on Aria's voice, blocking out the panic. "How do I stabilize it?"</p>

            <p>"Feel the boundary's natural state," Aria instructs, stepping closer. "It wants to close. Stop forcing it open and guide it back to equilibrium."</p>

            <p><span class="polly-comment">"Listen to the scary competent lady. She knows what she's talking about."</span></p>

            <p>You shift your approach - instead of controlling the portal, you <em>listen</em> to it. The boundary does have a natural state, and you can feel how it wants to return to stability.</p>

            <p>Gently, carefully, you guide rather than force. The crackling energy calms. The portal shrinks, then seals.</p>

            <p>Aria nods with satisfaction. "Well done. You trusted instruction over instinct, and you adapted your technique mid-crisis. That's the mark of a disciplined mage."</p>

            <p>Izack approaches. "And you learned to listen to the magic itself. Both of you taught the same lesson from different angles."</p>
        `,
        choices: [
            {
                text: "Thank Aria and ask to study more boundary techniques with her",
                next: 'ending_boundary_specialist',
                effects: { collaboration: 1, aria: 4, izack: 1 }
            },
            {
                text: "Thank both teachers and commit to learning collaborative magic going forward",
                next: 'ending_balanced_mage',
                effects: { collaboration: 2, aria: 2, izack: 2 }
            }
        ]
    },

    crisis_disaster: {
        text: `
            <p>You pour more power into the destabilizing portal, determined to force it under control.</p>

            <p><span class="polly-comment">"NO! Bad student! BAD-"</span></p>

            <p>The portal explodes outward. You're thrown backward as dimensional energy floods the chamber.</p>

            <p>Aria's voice cuts through reality itself: "BOUNDARY SEAL!"</p>

            <p>A wall of pure force slams down around the portal. Izack joins her, and together they compress the dimensional rupture back into stability. The effort leaves both of them visibly drained.</p>

            <p>The chamber falls silent except for heavy breathing.</p>

            <p>Aria turns to you, her expression cold. "That was reckless. You prioritized ego over safety and nearly breached dimensional barriers that protect this entire academy."</p>

            <p>Izack's disappointment is somehow worse than Aria's anger. "We teach collaboration here because <em>individual power has limits</em>. You just proved why."</p>

            <p><span class="polly-comment">"Yeah, this is... not great. You really messed up."</span></p>
        `,
        choices: [
            {
                text: "Genuinely apologize and ask for a chance to learn from this mistake",
                next: 'ending_humbled_student',
                effects: { collaboration: 0, izack: 0, aria: 0 }
            },
            {
                text: "Defend your approach - you were trying to solve it yourself",
                next: 'ending_expelled',
                effects: { collaboration: -3, izack: -2, aria: -2 }
            }
        ]
    },

    crisis_passive: {
        text: `
            <p>You step back, watching as Izack and Aria work together to seal the fracture. Their magic interweaves perfectly - his intuitive feel for dimensional currents, her precise boundary control.</p>

            <p>The crack seals. Crisis averted.</p>

            <p><span class="polly-comment">"So... you just watched. That's a choice."</span></p>

            <p>Izack turns to you, his expression gentle but serious. "You had the ability to help. Instead, you chose to be a bystander."</p>

            <p>Aria adds, "In collaborative environments, passive observation is a form of failure. Your classmates needed you."</p>

            <p>Zara looks hurt. "We're supposed to work together here."</p>

            <p><span class="polly-comment">"Harsh but true. Avalon isn't the place for people who watch others do the work."</span></p>
        `,
        choices: [
            {
                text: "Acknowledge the mistake and commit to being more engaged",
                next: 'ending_second_chance',
                effects: { collaboration: 0, izack: 0, zara: 0 }
            }
        ]
    },

    // ENDINGS

    ending_collaborative_master: {
        text: `
            <p><strong>Ending: The Collaborative Master</strong></p>

            <p>Three months later, you stand before the Spiral Spire, leading a group of seven students in a collaborative casting that creates a stable interdimensional bridge. What took Izack years to master, you and your team accomplished through perfect harmonic resonance.</p>

            <p><span class="polly-comment">"I've watched Avalon grow for years, and I can honestly say you're one of the finest examples of what this place is meant to create. Collaborative magic flows through you like breathing. Also, you're still terrible at morning portal crossings, but nobody's perfect."</span></p>

            <p>Izack approaches with tears of pride. "You've become everything I hoped Avalon could teach. Not a powerful mage who works with others - but a collaborative mage whose power comes <em>from</em> working with others."</p>

            <p>Aria nods. "You understand boundaries not as barriers but as bridges. The Third Thread flows strongest through those who truly embrace connection."</p>

            <p>Zara grins, bumping your shoulder. "Plus you're a really good friend. That matters too."</p>

            <p><span class="polly-comment">"Your story's just beginning, but what a beginning it's been. Go forth and be insufferably collaborative. Avalon's counting on it."</span></p>

            <p><em>You've discovered the true heart of Avalon: magic is strongest when shared, boundaries are meant to connect rather than divide, and the greatest power comes from listening and collaboration.</em></p>

            <p><strong>Collaboration Score: Transcendent</strong></p>
            <p><strong>Relationships: Deep bonds with Izack, Aria, and Zara</strong></p>
        `,
        choices: []
    },

    ending_collaborative_scholar: {
        text: `
            <p><strong>Ending: The Collaborative Scholar</strong></p>

            <p>Weeks pass as you immerse yourself in studying the Third Thread. Your research, conducted alongside Zara and other students, reveals new harmonics in collaborative magic that even Izack hadn't documented.</p>

            <p><span class="polly-comment">"Look at you, turning collaboration into a science. Izack's thrilled. He's been writing 'Wingscroll' notes about your discoveries for days."</span></p>

            <p>Izack reviews your latest findings. "This is remarkable. You're not just practicing collaborative magic - you're expanding our understanding of it. This will help future students immensely."</p>

            <p>Aria adds, "And you're doing it the right way - testing with partners, documenting failures as well as successes, building knowledge that others can build upon."</p>

            <p>Zara beams. "We make a good research team!"</p>

            <p><span class="polly-comment">"You've learned that magic isn't just about doing - it's about understanding, sharing, and building something bigger than yourself. That's the Avalon way."</span></p>

            <p><em>You've become a scholar of collaborative magic, dedicating yourself to understanding and teaching the principles that make Avalon unique.</em></p>

            <p><strong>Collaboration Score: Exemplary</strong></p>
            <p><strong>Relationships: Strong bonds with Izack, Zara, and the scholarly community</strong></p>
        `,
        choices: []
    },

    ending_balanced_mage: {
        text: `
            <p><strong>Ending: The Balanced Mage</strong></p>

            <p>Your training continues under both Izack and Aria, learning to balance intuitive collaboration with precise technique. You're equally comfortable in group harmonics and solo boundary work.</p>

            <p><span class="polly-comment">"You've become what Aria and Izack are together - someone who can feel the magic AND understand its mechanics. That's actually pretty rare."</span></p>

            <p>Aria observes your latest exercise with approval. "You've developed both sensitivity and discipline. That combination makes you versatile - able to adapt to any magical situation."</p>

            <p>Izack nods. "You understand that collaboration and individual skill aren't opposites. They support each other. Your solo work makes you a better partner, and your partnership work makes you a better individual mage."</p>

            <p><span class="polly-comment">"Plus you can work with pretty much anyone now. The overly cautious types, the wild experimenters, even the occasional visiting dignitary who doesn't understand Avalon's methods. You translate between approaches."</span></p>

            <p><em>You've mastered the balance between collaboration and individual expertise, becoming a bridge between different magical philosophies.</em></p>

            <p><strong>Collaboration Score: Strong</strong></p>
            <p><strong>Relationships: Respected by both Izack and Aria, trusted by peers</strong></p>
        `,
        choices: []
    },

    ending_boundary_specialist: {
        text: `
            <p><strong>Ending: The Boundary Specialist</strong></p>

            <p>Under Aria's intensive mentorship, you've become exceptionally skilled in dimensional boundary work. Your precision and control are remarkable, and you understand dimensional mechanics at a deep level.</p>

            <p><span class="polly-comment">"You took the Aria route - discipline, precision, and respect for boundaries. Not as flashy as collaborative harmonics, but you're the person everyone calls when portals start acting weird."</span></p>

            <p>Aria regards you with something close to pride. "You've developed the patience and precision that boundary work requires. You understand that dimensional magic isn't about force - it's about respect for what boundaries are and what they protect."</p>

            <p>Izack approaches. "And you're learning to incorporate collaborative elements into your work. Boundaries exist to connect realms, after all. You're understanding them as Aria does - as bridges, not walls."</p>

            <p><span class="polly-comment">"You're becoming Avalon's next boundary guardian. That's important work. Less cuddly than group harmonics, but somebody has to make sure the dimensional infrastructure doesn't collapse."</span></p>

            <p><em>You've specialized in boundary magic under Aria's guidance, becoming a guardian of dimensional stability and an expert in the structures that connect realms.</em></p>

            <p><strong>Collaboration Score: Moderate</strong></p>
            <p><strong>Relationships: Deeply mentored by Aria, respected by Izack</strong></p>
        `,
        choices: []
    },

    ending_humbled_student: {
        text: `
            <p><strong>Ending: The Humbled Student</strong></p>

            <p>Your apology was genuine, and over the following weeks, you prove it through actions. You approach every lesson with humility, ask for help readily, and prioritize safety over ego.</p>

            <p><span class="polly-comment">"You know what? You actually learned from screwing up. That's rarer than you'd think. Most people just make excuses."</span></p>

            <p>Izack watches as you successfully complete a collaborative exercise. "Failure can be the greatest teacher if we let it. You let it teach you."</p>

            <p>Aria's approval comes slowly, but it comes. "You showed me that you value safety and collaboration over pride. That's what I needed to see."</p>

            <p>Zara offers you a reassuring smile. "Everyone makes mistakes. What matters is what you do after."</p>

            <p><span class="polly-comment">"Your journey at Avalon started rough, but you're on solid ground now. Keep this humility, and you'll go far."</span></p>

            <p><em>You learned that pride comes before the fall, but humility can turn failure into growth. Your path at Avalon continues with a deeper understanding of your own limitations and the value of collaboration.</em></p>

            <p><strong>Collaboration Score: Growing</strong></p>
            <p><strong>Relationships: Rebuilding trust with teachers and peers</strong></p>
        `,
        choices: []
    },

    ending_second_chance: {
        text: `
            <p><strong>Ending: The Second Chance</strong></p>

            <p>You commit to being more engaged, and Avalon gives you that opportunity. Over the next weeks, you push yourself to participate, to reach out, to be present in collaborative work.</p>

            <p><span class="polly-comment">"You're trying. I'll give you that. Still a bit hesitant sometimes, but you're showing up."</span></p>

            <p>Zara tentatively partners with you again. "I can see you're making an effort. That means something."</p>

            <p>Izack's encouragement is gentle but firm. "Collaboration is a skill like any other. It takes practice, especially if it doesn't come naturally. Keep working at it."</p>

            <p>Aria observes from a distance, withholding final judgment but willing to let you prove yourself.</p>

            <p><span class="polly-comment">"Avalon believes in second chances, but not thirds. Make this one count."</span></p>

            <p><em>You're learning to move from observer to participant, slowly building the collaborative skills that Avalon values. Your story is still being written.</em></p>

            <p><strong>Collaboration Score: Learning</strong></p>
            <p><strong>Relationships: Tentative but improving</strong></p>
        `,
        choices: []
    },

    ending_expelled: {
        text: `
            <p><strong>Ending: The Rejected Thread</strong></p>

            <p>Your refusal to accept responsibility seals your fate. Aria's expression turns to ice.</p>

            <p>"Avalon was founded on principles of collaboration, safety, and growth through listening. You've demonstrated you value none of these things."</p>

            <p>Izack looks genuinely sad. "I wanted to believe you could learn here. But Avalon requires students who will protect each other, not endanger them for personal pride."</p>

            <p><span class="polly-comment">"Yeah, this is... this is not going to end well for you."</span></p>

            <p>Aria continues, "You're dismissed from Avalon Academy. Your portal access is revoked. I'll personally ensure you return safely to your home realm, but you are not welcome to return."</p>

            <p>As you're escorted to the departure gate, Polly lands on a nearby perch.</p>

            <p><span class="polly-comment">"You had every opportunity to learn, to grow, to be part of something amazing. You chose ego instead. I hope someday you understand what you lost here. Caw."</span></p>

            <p>The portal opens. Your brief time at Avalon ends in failure.</p>

            <p><em>Some lessons are learned too late. Avalon was not the place for you - not because you lacked talent, but because you refused to embrace what it teaches: that true power comes from collaboration, not domination.</em></p>

            <p><strong>Collaboration Score: Failed</strong></p>
            <p><strong>Relationships: Severed</strong></p>
        `,
        choices: []
    },

    // NEW EXPANDED CONTENT - Exploring the Realms

    field_expedition_offer: {
        text: `
            <p>After your successful first lesson, Izack gathers the class with exciting news.</p>

            <p>"Avalon has grown far beyond what I originally imagined," he says, eyes bright with wonder. "This realm now spans multiple biomes - forests that think, oceans that remember the past, deserts lit by eternal flame. We've arranged field expeditions for advanced students to explore these regions."</p>

            <p><span class="polly-comment">"Translation: he accidentally created a small planet and now needs students to go poke around and make sure nothing's trying to eat the academy. It's educational AND practical!"</span></p>

            <p>Aria steps forward with a crystalline map that shifts and glows. "We have three expeditions departing tomorrow. Each will teach different aspects of magic through direct environmental interaction."</p>

            <p>She points to three glowing regions on the map:</p>

            <p>"The <strong>Singing Dunes</strong> - a desert where the sand responds to truth and lies. You'll learn about honesty in magic and oath-binding."</p>

            <p>"The <strong>Verdant Tithe</strong> - an ancient forest where every thought has weight. Perfect for studying the connection between mind and nature."</p>

            <p>"The <strong>Rune Glacier</strong> - a constantly shifting ice field inscribed with living spells. Ideal for those who want to understand written magic at its most dynamic."</p>

            <p><span class="polly-comment">"Choose wisely. Each one will try to kill you in completely different ways. I'll be supervising the Dunes trip because watching students panic when the sand starts screaming never gets old."</span></p>
        `,
        choices: [
            {
                text: "Volunteer for the Singing Dunes expedition with Polly",
                next: 'singing_dunes_journey',
                effects: { collaboration: 1, aria: 1 }
            },
            {
                text: "Join the Verdant Tithe forest exploration",
                next: 'verdant_tithe_journey',
                effects: { collaboration: 2, izack: 1 }
            },
            {
                text: "Request the Rune Glacier - you want to master written magic",
                next: 'rune_glacier_journey',
                effects: { collaboration: 0, aria: 2 }
            }
        ]
    },

    singing_dunes_journey: {
        text: `
            <p>The portal deposits your expedition group onto golden sand that gleams with crystalline fragments. The heat hits you immediately, but it's the <em>sound</em> that's unforgettable.</p>

            <p>The dunes are humming.</p>

            <p>A low, haunting chorus rises from the desert itself - like a thousand voices singing just below the threshold of words. The sound shifts with each step you take.</p>

            <p><span class="polly-comment">*Landing on a sun-bleached stone* "Welcome to Sul'dessar, specifically the Sunscarred Dunes. This sand has a nasty habit of glowing red-hot when someone breaks an oath. Also, mirages here aren't just illusions - they're actual memories the desert preserved. Try not to walk into any traumatic historical events."</span></p>

            <p>Your group's guide, a weathered desert mage named Kael, gestures to an oasis shimmering in the distance. "We camp there tonight. But first - a test."</p>

            <p>He hands each student a small crystal vial. "Fill this with sand while speaking a truth about yourself. The desert will judge whether you're honest. If you lie..." He points to a patch of sand glowing angry crimson. "That's what happens."</p>

            <p>The other students nervously approach the dunes. You kneel and scoop sand, preparing to speak.</p>

            <p><span class="polly-comment">"This should be entertaining. The dunes are listening."</span></p>
        `,
        choices: [
            {
                text: "Speak a vulnerable truth: 'I'm afraid I'm not strong enough to make a difference here'",
                next: 'dunes_honest_truth',
                effects: { collaboration: 2, aria: 2 }
            },
            {
                text: "Share something safe: 'I want to learn everything Avalon can teach'",
                next: 'dunes_safe_truth',
                effects: { collaboration: 1 }
            },
            {
                text: "Test the desert's limits with an exaggeration: 'I'm destined to be the greatest mage of my generation'",
                next: 'dunes_rejected',
                effects: { collaboration: -1 }
            }
        ]
    },

    dunes_honest_truth: {
        text: `
            <p>As your words leave your lips, the sand in your vial begins to glow - not red with anger, but soft gold like sunrise.</p>

            <p>The humming of the dunes shifts into something that sounds almost like... approval? The tone warms, and you feel the desert's ancient attention settle on you like a gentle hand.</p>

            <p>Kael nods, impressed. "The desert respects vulnerability more than bravado. That sand you're holding is now <em>truth-sworn</em>. It will glow in the presence of deception - a valuable tool for a mage who values honesty."</p>

            <p><span class="polly-comment">"Well, well. The desert likes you. That's rare. Most students try to sound impressive and end up with screaming sand. You just earned yourself an actual magical artifact by being honest about your fears. There's a lesson in that."</span></p>

            <p>Over the next three days, your expedition explores the Singing Dunes. You witness oath-bound sand spirits emerging at twilight, visit an Ironwood oasis where trees harder than metal provide shelter, and learn to navigate by listening to the desert's song.</p>

            <p>On the final night, as mirages dance under the stars, Kael teaches your group the art of oath-magic - binding promises to the land itself.</p>

            <p>"In times of great need," he explains, "a promise made here and kept elsewhere strengthens both you and the desert. You become part of its song."</p>

            <p><span class="polly-comment">"You've learned that magic isn't just about power - it's about truth, trust, and being willing to be vulnerable. The desert taught you what Avalon's been trying to say all along."</span></p>
        `,
        choices: [
            {
                text: "Return to Avalon with your truth-sworn sand and new understanding",
                next: 'ending_truthbound_mage',
                effects: { collaboration: 2, aria: 2 }
            }
        ]
    },

    dunes_safe_truth: {
        text: `
            <p>The sand accepts your words - not glowing, but remaining neutral. It's true enough that the desert doesn't reject it, but not deep enough to earn its favor.</p>

            <p>Kael observes. "Acceptable. The desert allows surface truths, though it reserves its blessings for deeper honesty."</p>

            <p><span class="polly-comment">"You played it safe. Nothing wrong with that, but you also didn't get the special desert blessing the really honest students receive. In magic, as in life, you get out what you put in."</span></p>

            <p>The expedition continues. You learn about the Singing Dunes, witness sand spirits, and study oath-magic from a distance. It's educational and safe.</p>

            <p>But you can't help noticing that some of your fellow students - those who spoke vulnerable truths - seem to hear the desert's song more clearly than you do.</p>
        `,
        choices: [
            {
                text: "Return to Avalon with solid knowledge but no special connection",
                next: 'ending_balanced_mage',
                effects: { collaboration: 1 }
            }
        ]
    },

    dunes_rejected: {
        text: `
            <p>The moment your exaggeration leaves your mouth, the sand in your vial flares crimson and erupts into scorching heat. You drop it with a yelp.</p>

            <p>Around you, the entire dune begins to glow angry red. The humming shifts into something discordant - almost like screaming.</p>

            <p><span class="polly-comment">"And THERE it is! The desert does NOT appreciate arrogance masquerading as truth. I warned you the sand would judge."</span></p>

            <p>Kael quickly draws a circle of protection around you as the sand settles, still glowing faintly. "The Sunscarred Dunes punish those who lie to themselves most of all. Claiming destinies you haven't earned is the worst kind of falsehood here."</p>

            <p>The rest of the expedition becomes a lesson in humility. The desert refuses to teach you its deeper secrets, and the oath-spirits avoid you entirely.</p>

            <p>By the time you return to Avalon, you've learned about the Singing Dunes... but from the outside, as one the desert rejected.</p>
        `,
        choices: [
            {
                text: "Return to Avalon, humbled by the experience",
                next: 'ending_humbled_student',
                effects: { collaboration: 0 }
            }
        ]
    },

    verdant_tithe_journey: {
        text: `
            <p>The portal opens onto an ocean of green. Trees larger than Avalon's towers rise into mist, their canopy creating a twilight world below. The air itself feels <em>alive</em> - thick with the scent of growing things and something else... awareness.</p>

            <p>Izack leads this expedition personally. "Welcome to the Verdant Tithe, one of Avalon's transplanted biomes drawn from the ancient forests of Nirestal. Here, every thought has weight."</p>

            <p>As if to demonstrate, a vine near you shifts, reaching toward a student who's thinking intensely about their family. The plant seems to sense the emotion.</p>

            <p><span class="polly-comment">*Perched on Izack's shoulder* "The Thoughtvines are just the beginning. In the deep forest, the trees themselves remember every person who's passed through. Try to keep your mind calm - anxious thoughts attract attention you don't want."</span></p>

            <p>Izack nods. "The Tithe takes a piece of your consciousness as payment for passage - usually just surface thoughts or recent memories. In return, it offers guidance and protection. But you must learn to quiet your mind."</p>

            <p>Your group begins walking the forest path. Around you, luminescent fungi bloom in response to your footsteps, and you swear you can hear whispers in the rustling leaves.</p>

            <p>Suddenly, the path ahead splits into three directions. Each trail seems to call to different aspects of your mind.</p>

            <p>Izack smiles. "The forest is testing you. Choose the path that resonates, but understand - each leads to a different lesson."</p>
        `,
        choices: [
            {
                text: "Take the path lined with silver Dreamwillow trees - you sense visions there",
                next: 'dreamwillow_path',
                effects: { collaboration: 1, izack: 2 }
            },
            {
                text: "Follow the trail where Thoughtvines grow thickest - you want to understand the forest's mind",
                next: 'thoughtvine_path',
                effects: { collaboration: 2, zara: 1 }
            },
            {
                text: "Choose the path leading to a distant glow - the Heartwood Tree awaits",
                next: 'heartwood_path',
                effects: { collaboration: 3, izack: 2 }
            }
        ]
    },

    dreamwillow_path: {
        text: `
            <p>The Dreamwillow grove is breathtaking. Silver leaves shimmer overhead, and the air is heavy with possibility. Izack gestures for the group to sit beneath the largest tree.</p>

            <p>"Dreamwillows show visions of possible futures," he explains softly. "But be warned - they show <em>all</em> possibilities, not just pleasant ones. The forest wants you to understand that every choice branches reality."</p>

            <p>As you lean against the silvery bark, drowsiness overtakes you. Your vision blurs, and suddenly you're seeing...</p>

            <p>...yourself, years older, standing at the heart of Avalon's Spiral Spire, guiding dozens of students through a complex collaborative spell. The vision feels warm, right.</p>

            <p>...yourself, alone in a tower, surrounded by books and power, having mastered magic but lost all your connections. Cold. Empty.</p>

            <p>...yourself, standing at a threshold between Avalon and the demon realm Varn'ka'zul, making a choice that will determine the fate of both worlds.</p>

            <p>The visions fade. You gasp, returning to the present.</p>

            <p><span class="polly-comment">"The Dreamwillows don't tell you which future is 'right.' They just show you that your choices matter. What you do now echoes forward."</span></p>

            <p>Izack places a hand on your shoulder. "The forest has shown you its deepest lesson: magic is choice, and every choice shapes not just you, but the world around you."</p>
        `,
        choices: [
            {
                text: "Embrace the vision of collaborative teaching - that's the future you'll work toward",
                next: 'ending_collaborative_scholar',
                effects: { collaboration: 3, izack: 3 }
            },
            {
                text: "The visions trouble you - ask Izack how to ensure you choose wisely",
                next: 'ending_balanced_mage',
                effects: { collaboration: 2, izack: 2 }
            }
        ]
    },

    thoughtvine_path: {
        text: `
            <p>The Thoughtvines grow so thick here that they form living walls, pulsing gently with bioluminescent light. As you walk among them, you feel your thoughts becoming... shared.</p>

            <p>It's not invasive - more like your consciousness is expanding to include the forest itself. You can sense the other students' wonder, Izack's pride, Polly's amused observation.</p>

            <p>And beneath it all, the forest's vast, ancient mind.</p>

            <p><span class="polly-comment">"This is what the Third Thread feels like - consciousness braiding together. Not domination, not submission, just... connection. Multiple minds becoming something greater."</span></p>

            <p>A memory that isn't yours surfaces: you see this forest centuries ago, feel the Dryads singing it into awareness, experience the moment it first began to <em>think</em>.</p>

            <p>Izack's voice cuts through gently. "You're experiencing the forest's living memory. It's offering you a gift - understanding of how collaboration at the deepest level feels."</p>

            <p>The vines pulse brighter, and you feel a question form in your mind - not in words, but in pure meaning:</p>

            <p><em>Will you remember me? Will you carry this connection forward?</em></p>

            <p>The forest wants to know if you'll honor what you've learned here.</p>
        `,
        choices: [
            {
                text: "Promise to carry the forest's lesson of connection with you always",
                next: 'ending_forestbound_mage',
                effects: { collaboration: 4, izack: 3, zara: 2 }
            },
            {
                text: "Accept the gift gratefully but make no binding promises",
                next: 'ending_collaborative_scholar',
                effects: { collaboration: 2, izack: 2 }
            }
        ]
    },

    heartwood_path: {
        text: `
            <p>The path leads deep into the forest's heart. The trees here are impossibly ancient, their bark inscribed with natural runes that glow faintly. At the center stands a tree unlike any other.</p>

            <p>The Heartwood Tree.</p>

            <p>It's massive beyond belief, with bark that seems to pulse like a heartbeat and roots that disappear into glowing earth. You can feel its awareness - vast, patient, kind but utterly inhuman.</p>

            <p><span class="polly-comment">*Unusually quiet* "This is one of the oldest living things in any realm. It was here before Avalon, before Izack, before most of what we call civilization. It's the forest's heart and mind made manifest."</span></p>

            <p>Izack bows respectfully to the tree. "The Heartwood only reveals itself to those it wishes to teach. You've been called here."</p>

            <p>As you approach, the tree's roots shift, creating a natural seat at its base. The moment you sit, understanding floods through you:</p>

            <p>You feel the interconnection of all living things - how every breath you take feeds the plants, how every plant's gift feeds you. You understand that magic isn't something you <em>do</em>, it's something you <em>participate in</em>.</p>

            <p>The Heartwood offers you a single fruit - golden, glowing with concentrated life essence.</p>

            <p>Izack's eyes widen. "I've visited this tree a hundred times. It's never offered its fruit before."</p>

            <p><span class="polly-comment">"If you eat that, you'll be bonded to the forest forever. You'll carry a piece of the Verdant Tithe in your soul. That's not a small thing."</span></p>
        `,
        choices: [
            {
                text: "Accept the fruit and bond with the forest's ancient wisdom",
                next: 'ending_heartwood_guardian',
                effects: { collaboration: 5, izack: 4, zara: 2 }
            },
            {
                text: "Politely decline - the gift is too great, and you're not ready for that bond",
                next: 'ending_humble_seeker',
                effects: { collaboration: 2, izack: 3 }
            }
        ]
    },

    rune_glacier_journey: {
        text: `
            <p>The temperature drops the moment you step through the portal. You're standing on ice that glows from within, inscribed with shifting runic patterns that rearrange themselves as you watch.</p>

            <p>Aria leads this expedition, her bearing regal even in the arctic cold. "The Rune Glacier is one of Avalon's most dangerous teaching environments. The ice remembers every spell ever cast here and rewrites itself constantly."</p>

            <p><span class="polly-comment">*Fluffing her feathers against the cold* "It's like trying to read a book that's rewriting itself while you're reading it. Students who can't adapt freeze in time pockets or get lost in recursive spell loops. Fun!"</span></p>

            <p>Aria gestures across the ice field. "Your task: navigate to the central chamber where an ancient spell-library is frozen. The glacier will test your ability to read, interpret, and respond to written magic in real-time."</p>

            <p>She hands each student a crystal stylus. "These can write on the ice temporarily. Use them to create paths, counter hostile runes, or communicate with the glacier itself. Some say it's sentient."</p>

            <p>As your group begins walking, the ice beneath your feet suddenly blazes with a rune of <strong>TRIAL</strong>. Three paths appear, each marked with different runic sequences.</p>

            <p>One path shows <em>Control</em> runes - straight lines, rigid structure, commanding magic.</p>

            <p>Another displays <em>Harmony</em> runes - flowing curves, collaborative patterns, responsive magic.</p>

            <p>The third path is blank ice - no runes at all, an unknown challenge.</p>

            <p>Aria watches you carefully. "Your choice of path will determine what the glacier teaches you."</p>
        `,
        choices: [
            {
                text: "Choose the Control path - master structured, disciplined magic",
                next: 'glacier_control_path',
                effects: { collaboration: -1, aria: 3 }
            },
            {
                text: "Take the Harmony path - learn responsive, flowing magic",
                next: 'glacier_harmony_path',
                effects: { collaboration: 2, aria: 2, izack: 1 }
            },
            {
                text: "Step onto the blank ice - embrace the unknown",
                next: 'glacier_mystery_path',
                effects: { collaboration: 1, aria: 2 }
            }
        ]
    },

    glacier_harmony_path: {
        text: `
            <p>The moment you step onto the Harmony path, the runes beneath your feet begin to sing - literally producing musical tones as they shift and flow.</p>

            <p>Aria walks beside you. "Good choice. The glacier responds best to those who work <em>with</em> it rather than trying to dominate it."</p>

            <p>As you progress, the ice presents challenges: a crevasse appears, but when you draw a bridging rune that complements the glacier's existing patterns, the ice itself forms a crossing. A frozen time-pocket threatens to trap a fellow student, but by writing a harmony rune that resonates with the glacier's frequency, you help free them.</p>

            <p><span class="polly-comment">"You're learning the glacier's language instead of forcing your own. This is exactly what Avalon teaches - magic as conversation, not command."</span></p>

            <p>After hours of navigation, you reach the central chamber. Here, countless spells are preserved in crystalline ice, forming a library of magical knowledge spanning centuries.</p>

            <p>Aria gestures to the frozen spells. "This is the Glacier's gift - every mage who's worked in harmony with it has left knowledge here. You've earned the right to learn from them."</p>

            <p>You spend days studying the frozen library, learning collaboration techniques from mages long dead but whose wisdom lives on in ice.</p>

            <p>When you finally leave, the glacier writes one last rune beneath your feet: <strong>FRIEND</strong>.</p>
        `,
        choices: [
            {
                text: "Return to Avalon with the glacier's friendship and ancient knowledge",
                next: 'ending_runeweaver',
                effects: { collaboration: 3, aria: 3, izack: 2 }
            }
        ]
    },

    // NEW ENDINGS

    ending_truthbound_mage: {
        text: `
            <p><strong>Ending: The Truthbound Mage</strong></p>

            <p>You return to Avalon carrying truth-sworn sand from the Singing Dunes and a profound understanding that magic begins with honesty - especially honesty with yourself.</p>

            <p>Over time, you become known as someone who can cut through deception, not through force but through simple, relentless truth. Your truth-sworn sand helps arbitrate disputes, reveals hidden intentions, and guides lost students back to themselves.</p>

            <p><span class="polly-comment">"You learned the hardest lesson: that vulnerability is strength, that admitting fear takes more courage than pretending confidence. The desert recognized that, and now so does everyone else."</span></p>

            <p>Aria approaches you months later with a proposal. "We need someone to establish a sister academy in the Singing Dunes - a place where oath-magic and truth-binding can be taught properly. Would you consider it?"</p>

            <p>Izack adds, "You've shown that Avalon's principles work anywhere - even in a desert that literally punishes lies. That's the kind of mage we need shaping the next generation."</p>

            <p><em>You've become a bridge between Avalon and the ancient wisdom of the Singing Dunes, proving that truth and vulnerability are the foundations of all real magic.</em></p>

            <p><strong>Collaboration Score: Exemplary</strong></p>
            <p><strong>Achievement: Bearer of Truth-Sworn Sand</strong></p>
        `,
        choices: []
    },

    ending_forestbound_mage: {
        text: `
            <p><strong>Ending: The Forestbound Guardian</strong></p>

            <p>You return from the Verdant Tithe forever changed. A piece of the forest's consciousness lives within you now - you can hear the whispers of growing things, sense the health of ecosystems, and understand the language of life itself.</p>

            <p>Thoughtvines grow wherever you spend time, and students notice that plants seem healthier in your presence. You've become a living bridge between civilization and the wild.</p>

            <p><span class="polly-comment">"You're basically a walking piece of the forest now. It's actually pretty beautiful, even if it means you occasionally sprout flowers when you're happy. Yes, that's a thing that happens. You'll get used to it."</span></p>

            <p>Izack is fascinated. "You've achieved something I've only theorized - true symbiosis between human consciousness and a living ecosystem. The forest chose you as its ambassador."</p>

            <p>Zara, herself a hybrid, understands. "You're like me now - belonging to multiple worlds, seeing connections others miss. It's a gift."</p>

            <p>The Verdant Tithe calls to you in dreams, and sometimes you return there, walking paths that appear only for you, learning secrets the forest shares with its chosen ones.</p>

            <p><em>You've become the Forestbound Guardian - a mage who embodies the living connection between mind and nature, proving that true magic is relationship, not dominion.</em></p>

            <p><strong>Collaboration Score: Transcendent</strong></p>
            <p><strong>Achievement: Friend of the Verdant Tithe</strong></p>
        `,
        choices: []
    },

    ending_heartwood_guardian: {
        text: `
            <p><strong>Ending: Guardian of the Heartwood</strong></p>

            <p>You eat the golden fruit, and the world explodes into connection.</p>

            <p>Every living thing in Avalon suddenly feels close - you sense the golem Clayborn's growing consciousness, the fish in Avalon's Time Ocean swimming through memory, the students' hopes and fears pulsing like heartbeats. You've become part of life's great web.</p>

            <p><span class="polly-comment">*Tears streaming* "Do you know what you just did? The Heartwood hasn't chosen a guardian in three thousand years. You're bonded to one of the oldest, wisest living things in existence. I'm actually crying. Caw."</span></p>

            <p>Izack kneels before you in respect. "You carry the forest's heart now. When you speak, ancient wisdom speaks through you. When you act, the pattern of life itself guides you."</p>

            <p>Aria's eyes show wonder. "I've spent my life studying boundaries. You just erased them - you exist in perfect balance between human and forest, individual and collective, mortal and eternal."</p>

            <p>Over the years, you become Avalon's living anchor - the one who ensures the realm stays connected to its purpose, who speaks for the voiceless, who reminds everyone that magic is life and life is sacred.</p>

            <p>When you eventually stand before the Spiral Spire in times of crisis, roots grow from your feet, leaves bloom in your hair, and the Heartwood's ancient power flows through you to heal, protect, and unite.</p>

            <p><em>You are the Guardian of the Heartwood - living proof that when you give yourself fully to connection, you become something greater than you ever imagined possible.</em></p>

            <p><strong>Collaboration Score: Transcendent Beyond Measure</strong></p>
            <p><strong>Achievement: Heartwood Guardian - Chosen of the Ancient Forest</strong></p>
        `,
        choices: []
    },

    ending_runeweaver: {
        text: `
            <p><strong>Ending: The Runeweaver</strong></p>

            <p>Your time at the Rune Glacier has transformed you into a master of written magic. You can read spells in ice, stone, and air. You understand that runes aren't just symbols - they're living conversations frozen into form.</p>

            <p>Aria takes you as a personal apprentice. "You've learned what took me decades - that the most powerful magic comes from working with existing patterns rather than imposing your own."</p>

            <p><span class="polly-comment">"You literally made friends with a sentient glacier. That's either brilliance or madness, and I'm honestly not sure which. Possibly both."</span></p>

            <p>Over time, you develop a unique specialty: you can write runes that adapt to their environment, spells that rewrite themselves to respond to changing conditions. Your defensive wards don't just protect - they learn and evolve.</p>

            <p>When a crisis threatens Avalon's boundaries, you're the one who inscribes the new protections - runes that sing in harmony with the realm's heartbeat, barriers that flex instead of break, defenses that collaborate rather than simply resist.</p>

            <p>The Rune Glacier sends you gifts sometimes: ice that won't melt, carrying new patterns for you to study. You've become its student for life.</p>

            <p><em>You are the Runeweaver - a mage who writes magic as living conversation, proving that the most enduring spells are those that work in harmony with the world.</em></p>

            <p><strong>Collaboration Score: Strong</strong></p>
            <p><strong>Achievement: Friend of the Rune Glacier</strong></p>
        `,
        choices: []
    },

    ending_humble_seeker: {
        text: `
            <p><strong>Ending: The Humble Seeker</strong></p>

            <p>You respectfully decline the Heartwood's fruit, bowing deeply to the ancient tree. "I'm honored beyond words, but I'm not ready for such a bond. I still have so much to learn."</p>

            <p>The Heartwood's awareness shifts - and you sense... approval? The tree's roots form a different pattern, and a single leaf falls into your hand - silver-edged, glowing faintly.</p>

            <p><span class="polly-comment">"The tree respects your honesty. By admitting you're not ready, you proved the wisdom it was looking for. That leaf is a promise - when you ARE ready, the Heartwood will remember you."</span></p>

            <p>Izack places a hand on your shoulder. "Knowing your limitations is its own form of strength. The Heartwood tested your humility as much as your potential."</p>

            <p>You return to Avalon with the Heartwood's leaf and a deep understanding that the best magic comes from knowing when to accept gifts and when to wait until you're truly ready to honor them.</p>

            <p>Your path continues - still learning, still growing, still seeking wisdom rather than rushing toward power.</p>

            <p><em>You are the Humble Seeker - a mage who understands that true wisdom often means acknowledging what you don't yet know.</em></p>

            <p><strong>Collaboration Score: Growing</strong></p>
            <p><strong>Achievement: Blessed by the Heartwood</strong></p>
        `,
        choices: []
    },

    glacier_control_path: {
        text: `
            <p>You choose the path of Control, and the glacier immediately challenges you. The runes under your feet lock into rigid patterns, demanding perfect execution.</p>

            <p>Aria watches as you navigate with precise, disciplined magic. "Control isn't wrong," she says, "but on this path, one mistake compounds into disaster."</p>

            <p>You progress through sheer will and technical skill, but it's exhausting. Every step requires perfect rune-writing, flawless execution. When a time-pocket opens, you force it closed through raw power rather than finesse.</p>

            <p><span class="polly-comment">"You're fighting the glacier instead of working with it. That takes strength, but it's the hard way."</span></p>

            <p>You reach the central library, but the knowledge here resists you. These spells were left by collaborative mages, and they don't respond well to domination.</p>

            <p>Aria intervenes. "You've proven your discipline. Now - are you willing to add flexibility to it?"</p>
        `,
        choices: [
            {
                text: "Admit control alone isn't enough - ask Aria to teach you harmony",
                next: 'ending_balanced_mage',
                effects: { collaboration: 1, aria: 3 }
            },
            {
                text: "Insist your approach works - you just need more practice",
                next: 'ending_boundary_specialist',
                effects: { collaboration: 0, aria: 2 }
            }
        ]
    },

    glacier_mystery_path: {
        text: `
            <p>You step onto blank ice, and immediately the world shifts. The glacier shows you its true nature - not a static library, but a living entity that's been watching, learning, evolving for centuries.</p>

            <p>The ice beneath you becomes a mirror, reflecting not your image but your <em>potential</em>. You see paths you could take, mages you could become, futures branching like frost patterns.</p>

            <p><span class="polly-comment">"Oh. Oh, the glacier is showing you something it's never shown anyone else. This is... actually I have no idea what this is."</span></p>

            <p>Aria's voice is awed. "The glacier is offering you a choice no other student has faced. It wants to know - will you help it grow? Will you teach it as much as you learn from it?"</p>

            <p>The runes ask a question in pure meaning: <em>Will you be my partner, not my master or my student, but my equal?</em></p>

            <p>This is unprecedented. The glacier wants symbiosis - to learn from you as you learn from it.</p>
        `,
        choices: [
            {
                text: "Accept the glacier's offer of partnership - grow together",
                next: 'ending_glacier_partner',
                effects: { collaboration: 5, aria: 4, izack: 3 }
            },
            {
                text: "Decline gently - partnership with a glacier is beyond you right now",
                next: 'ending_humble_seeker',
                effects: { collaboration: 2, aria: 3 }
            }
        ]
    },

    ending_glacier_partner: {
        text: `
            <p><strong>Ending: Partner of the Rune Glacier</strong></p>

            <p>You accept, and the blank ice blazes with new runes - a collaborative script written by you and the glacier together, creating magic that's never existed before.</p>

            <p><span class="polly-comment">*Absolutely stunned* "You just... you and a sentient glacier just invented a new form of magic. Together. I don't... I have no words. That's never happened in recorded history."</span></p>

            <p>Aria kneels in the snow, touching the new runes with wonder. "This is the Third Thread manifested in written magic. Human and environment, thought and element, becoming equals in creation."</p>

            <p>From that day forward, you and the glacier work as partners. You teach it about human emotion, creativity, hope. It teaches you about patience, eternity, the slow wisdom of ice. Together, you develop spells that adapt and evolve, magic that learns.</p>

            <p>Other mages come to study what you've created. The glacier opens itself to them differently now - no longer just a testing ground, but a teacher that learned how to teach from you.</p>

            <p>Izack visits months later, tears in his eyes. "This is what I dreamed Avalon could inspire - true partnership between mages and the world itself. You've become something entirely new."</p>

            <p><em>You are the Glacier's Partner - the first mage to achieve true equality with an elemental force, proving that magic's highest form is mutual creation.</em></p>

            <p><strong>Collaboration Score: Revolutionary</strong></p>
            <p><strong>Achievement: Co-Creator with the Rune Glacier</strong></p>
        `,
        choices: []
    }
}
};

// UI Update Functions
function updateStats() {
    const collabPercent = Math.max(0, Math.min(100, 50 + (gameState.collaborationScore * 10)));
    document.getElementById('collaboration-bar').style.width = collabPercent + '%';
    document.getElementById('collaboration-value').textContent = gameState.collaborationScore;

    // Update relationship displays
    const getEmoji = (value) => {
        if (value >= 3) return '😊';
        if (value >= 1) return '🙂';
        if (value <= -2) return '😠';
        if (value <= -1) return '😕';
        return '😐';
    };

    document.getElementById('izack-rel').textContent = `Izack: ${getEmoji(gameState.relationships.izack)}`;
    document.getElementById('aria-rel').textContent = `Aria: ${getEmoji(gameState.relationships.aria)}`;
    document.getElementById('zara-rel').textContent = `Zara: ${getEmoji(gameState.relationships.zara)}`;
}

function displayNode(nodeId) {
    const node = storyNodes[nodeId];
    if (!node) return;

    gameState.currentNode = nodeId;

    traceEvent('node_displayed', {
        node: nodeId,
        collaborationScore: gameState.collaborationScore,
        relationships: { ...gameState.relationships }
    });

    // Display story text
    document.getElementById('story-text').innerHTML = node.text;

    // Display choices
    const choicesDiv = document.getElementById('choices');
    choicesDiv.innerHTML = '';

    if (node.choices.length === 0) {
        // This is an ending
        document.getElementById('restart-btn').style.display = 'block';
        traceEvent('ending_reached', {
            ending: nodeId,
            collaborationScore: gameState.collaborationScore,
            relationships: { ...gameState.relationships },
            path: gameState.choices.slice()
        });
    } else {
        node.choices.forEach((choice, index) => {
            const button = document.createElement('button');
            button.className = 'choice-btn';
            button.innerHTML = choice.text;
            button.onclick = () => makeChoice(choice);
            choicesDiv.appendChild(button);
        });
    }

    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function makeChoice(choice) {
    // Apply effects
    if (choice.effects) {
        if (choice.effects.collaboration !== undefined) {
            gameState.collaborationScore += choice.effects.collaboration;
        }
        if (choice.effects.izack !== undefined) {
            gameState.relationships.izack += choice.effects.izack;
        }
        if (choice.effects.aria !== undefined) {
            gameState.relationships.aria += choice.effects.aria;
        }
        if (choice.effects.zara !== undefined) {
            gameState.relationships.zara += choice.effects.zara;
        }
    }

    // Record choice
    gameState.choices.push({
        node: gameState.currentNode,
        choice: choice.text
    });

    traceEvent('choice_made', {
        fromNode: gameState.currentNode,
        choiceText: choice.text,
        effects: choice.effects || {},
        updatedCollaboration: gameState.collaborationScore,
        relationships: { ...gameState.relationships }
    });

    // Update stats
    updateStats();

    // Move to next node
    displayNode(choice.next);
}

function restartGame() {
    gameState.currentNode = 'start';
    gameState.collaborationScore = 0;
    gameState.relationships = {
        izack: 0,
        aria: 0,
        zara: 0
    };
    gameState.choices = [];

    document.getElementById('restart-btn').style.display = 'none';
    updateStats();
    displayNode('start');
    traceEvent('game_restarted', {});
}

// Initialize game
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('restart-btn').onclick = restartGame;
    updateStats();
    displayNode('start');
    traceEvent('init', {
        sessionId: window.gameTrace && window.gameTrace.sessionId,
        startNode: gameState.currentNode
    });
});
