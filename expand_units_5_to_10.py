import re, sys
sys.stdout.reconfigure(encoding='utf-8')

print("Building data for Units 5 to 10...")

# Function to build unit HTML
def build_unit_html(u_num, title, culture_title, culture_notes, dialogue_lines, video_url, video_text,
                    vocab_cat1_title, vocab_cat1_items, vocab_cat2_title, vocab_cat2_items,
                    grammar_title, grammar_rules, grammar_exercises,
                    listening_title, listening_items,
                    oral_title, oral_items,
                    reading_title, reading_text, reading_items,
                    writing_title, writing_items,
                    quiz_title, quiz_items):
    
    dialogue_html = ""
    dialogue_full_text = "Dialogue. "
    for speaker, text in dialogue_lines:
        dialogue_html += f'<p style="margin-bottom: 0.5rem;"><strong>{speaker}:</strong> {text}</p>\n'
        dialogue_full_text += f"{speaker} says: {text} "
    
    culture_html = f'''
        <!-- 🇺🇸 AMERICAN ENGLISH IN USE (OXFORD STYLE) -->
        <section class="culture-section" style="margin-top: 0 !important;">
            <h2 class="section-title">American Culture: {culture_title}</h2>

            <div class="reading-passage" id="am-text-{u_num}">
                <h3>📖 American Culture Notes</h3>
                <p>{culture_notes}</p>
                <div style="margin-top:1rem;">
                    <button class="audio-btn" onclick="speakText('{culture_notes.replace("'", "\\'")}')">🔊 Listen to Notes</button>
                    <button class="audio-btn stop" onclick="stopAudio()">⏹️ Stop</button>
                </div>
            </div>

            <div class="american-dialogue" id="am-dialogue-{u_num}">
                <h3>🗣️ Everyday Dialogue</h3>
                <div class="dialogue-box">
                    {dialogue_html}
                </div>
                <div style="margin-top:1rem;">
                    <button class="audio-btn" onclick="speakText('{dialogue_full_text.replace("'", "\\'")}')">🔊 Listen to Dialogue</button>
                    <button class="audio-btn stop" onclick="stopAudio()">⏹️ Stop</button>
                </div>
            </div>
            
            <p style="margin-top: 15px; font-size: 1.05rem; background: rgba(255, 154, 68, 0.1); padding: 0.8rem; border-radius: 8px; border-left: 4px solid var(--accent-orange);">
                🎥 <strong>Video Lesson:</strong> 
                <a href="{video_url}" target="_blank" style="color: var(--accent-indigo); text-decoration: underline; font-weight: bold;">
                    {video_text}
                </a>
            </p>
            <p class="material-reference" style="margin-top: 15px; font-size: 0.95rem; color: var(--text-secondary);"><strong>Free Study Materials:</strong> <a href="https://learningenglish.voanews.com/" target="_blank" style="color: var(--accent-indigo); text-decoration: none;">VOA Learning English</a> &bull; <a href="https://elt.oup.com/learning_resources" target="_blank" style="color: var(--accent-indigo); text-decoration: none;">Oxford English Resources</a></p>
        </section>
'''

    def render_vocab_grid(items):
        grid_html = '<div class="vocabulary-grid">\n'
        for word, defn, ex, icon in items:
            audio_text = f"{word}. {defn}. Example: {ex}".replace("'", "\\'")
            grid_html += f'''                <div class="vocab-card">
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <span style="font-size: 1.4rem;">{icon}</span>
                        <div class="vocab-word">{word}</div>
                    </div>
                    <div class="vocab-definition">{defn}</div>
                    <div class="vocab-example">"{ex}"</div>
                    <button class="audio-btn small" onclick="speakText('{audio_text}')">🔊 Play</button>
                </div>\n'''
        grid_html += '            </div>\n'
        return grid_html

    vocab_html = f'''
        <!-- SECTION 1: VOCABULARY BOOST -->
        <section class="section-wrapper" id="vocabulary-section-{u_num}">
            <span class="section-label vocabulary">📚 Section 1: Vocabulary Boost</span>
            <h2 class="section-title">{title} Vocabulary (20 Items)</h2>
            
            <h3 style="color:var(--accent-indigo);margin-bottom:1rem">Category 1: {vocab_cat1_title} (10 Items)</h3>
            {render_vocab_grid(vocab_cat1_items)}
            
            <h3 style="color:var(--accent-indigo);margin:2rem 0 1rem">Category 2: {vocab_cat2_title} (10 Items)</h3>
            {render_vocab_grid(vocab_cat2_items)}
        </section>
'''

    grammar_rules_html = ""
    for r_title, r_desc, r_example in grammar_rules:
        grammar_rules_html += f'''            <div class="grammar-rule">
                <strong>{r_title}:</strong> {r_desc} <span class="grammar-example">{r_example}</span>
            </div>\n'''

    grammar_ex_html = ""
    for idx, (q_text, opts, correct_val) in enumerate(grammar_exercises, 1):
        q_id = f"u{u_num}_g_ex{idx}"
        opts_html = "".join([f'<option value="{opt}">{opt}</option>' for opt in opts])
        grammar_ex_html += f'''                <div class="exercise-item exercise-question" data-question="{q_id}" style="margin-bottom:1rem;">
                    <p style="margin-bottom:0.4rem;"><strong>{idx}.</strong> {q_text}</p>
                    <div class="exercise-dropdown" style="display:flex; gap:0.5rem; align-items:center;">
                        <select data-correct="{correct_val}" style="padding:0.4rem 0.8rem; border-radius:6px; border:1px solid #cbd5e1;">
                            <option value="">-- Select --</option>
                            {opts_html}
                        </select>
                        <button class="check-answer-btn" onclick="checkDropdownAnswer('{q_id}')" style="padding:0.4rem 0.8rem; background:var(--accent-indigo); color:white; border:none; border-radius:6px; cursor:pointer;">Check</button>
                    </div>
                    <div class="feedback-message" style="margin-top:0.3rem; font-weight:bold;"></div>
                </div>\n'''

    grammar_html = f'''
        <!-- SECTION 2: GRAMMAR FOCUS -->
        <section class="grammar-box" id="grammar-section-{u_num}">
            <span class="section-label grammar">📝 Section 2: Grammar Focus</span>
            <h2 class="section-title">{grammar_title}</h2>
            {grammar_rules_html}
            
            <h3 style="color:var(--accent-indigo); margin: 1.5rem 0 1rem;">Grammar Practice Exercises (15 Items)</h3>
            <div class="exercise-box">
                {grammar_ex_html}
            </div>
        </section>
'''

    listening_items_html = ""
    for idx, (audio_t, q_text, opts, correct_idx) in enumerate(listening_items, 1):
        q_name = f"u{u_num}_list_q{idx}"
        opts_divs = ""
        for o_idx, opt in enumerate(opts):
            is_cor = "true" if o_idx == correct_idx else "false"
            opts_divs += f'''                    <div class="mc-option" style="margin: 0.3rem 0; padding: 0.4rem 0.8rem; border: 1px solid #cbd5e1; border-radius: 6px;">
                        <label style="cursor: pointer; display: flex; align-items: center; gap: 0.5rem;">
                            <input type="radio" name="{q_name}" data-correct="{is_cor}"> {opt}
                        </label>
                    </div>\n'''
        
        listening_items_html += f'''            <div class="mc-exercise" style="background: white; padding: 1rem; border-radius: 8px; margin-bottom: 1rem; box-shadow: 0 2px 4px rgba(0,0,0,0.04);">
                <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.5rem;">
                    <strong>Item {idx}:</strong> 
                    <button class="audio-btn small" onclick="speakText('{audio_t.replace("'", "\\'")}')">🔊 Listen</button>
                </div>
                <p style="margin-bottom: 0.5rem; font-weight: 500;">{q_text}</p>
                {opts_divs}
                <button class="mc-check-btn" onclick="checkMC('{q_name}')" style="margin-top: 0.5rem; padding: 0.3rem 0.8rem; background: var(--accent-orange); color: white; border: none; border-radius: 6px; cursor: pointer;">Check Answer</button>
                <div class="mc-feedback" style="margin-top: 0.4rem; font-weight: bold;"></div>
            </div>\n'''

    listening_html = f'''
        <!-- SECTION 3: LISTENING COMPREHENSION -->
        <section class="section-wrapper" id="listening-section-{u_num}">
            <span class="section-label listening">🎧 Section 3: Listening Comprehension</span>
            <h2 class="section-title">{listening_title} (15 Items)</h2>
            {listening_items_html}
        </section>
'''

    oral_items_html = ""
    for idx, (phrase, note) in enumerate(oral_items, 1):
        clean_phrase = phrase.replace("'", "\\'")
        oral_items_html += f'''            <div style="background: white; padding: 0.8rem 1.2rem; border-radius: 8px; margin-bottom: 0.8rem; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
                <div>
                    <strong>{idx}.</strong> <span style="font-size: 1.05rem; font-weight: 500;">"{phrase}"</span>
                    <div style="font-size: 0.85rem; color: #64748b; margin-top: 0.2rem;">💡 <em>{note}</em></div>
                </div>
                <div style="display: flex; gap: 0.4rem;">
                    <button class="audio-btn small" onclick="speakText('{clean_phrase}')">🔊 Normal</button>
                    <button class="audio-btn small" onclick="speakTextSlow('{clean_phrase}')">🐢 Slow</button>
                </div>
            </div>\n'''

    oral_html = f'''
        <!-- SECTION 4: PRONUNCIATION & ORAL DRILLS -->
        <section class="section-wrapper" id="oral-section-{u_num}">
            <span class="section-label speaking">🗣️ Section 4: Pronunciation & Oral Drills</span>
            <h2 class="section-title">{oral_title} (15 Drills)</h2>
            {oral_items_html}
        </section>
'''

    reading_items_html = ""
    for idx, (q_text, opts, correct_idx) in enumerate(reading_items, 1):
        q_name = f"u{u_num}_read_q{idx}"
        opts_divs = ""
        for o_idx, opt in enumerate(opts):
            is_cor = "true" if o_idx == correct_idx else "false"
            opts_divs += f'''                    <div class="mc-option" style="margin: 0.3rem 0; padding: 0.4rem 0.8rem; border: 1px solid #cbd5e1; border-radius: 6px;">
                        <label style="cursor: pointer; display: flex; align-items: center; gap: 0.5rem;">
                            <input type="radio" name="{q_name}" data-correct="{is_cor}"> {opt}
                        </label>
                    </div>\n'''
        
        reading_items_html += f'''            <div class="mc-exercise" style="background: white; padding: 1rem; border-radius: 8px; margin-bottom: 1rem; box-shadow: 0 2px 4px rgba(0,0,0,0.04);">
                <p style="margin-bottom: 0.5rem; font-weight: 500;"><strong>Question {idx}:</strong> {q_text}</p>
                {opts_divs}
                <button class="mc-check-btn" onclick="checkMC('{q_name}')" style="margin-top: 0.5rem; padding: 0.3rem 0.8rem; background: var(--accent-indigo); color: white; border: none; border-radius: 6px; cursor: pointer;">Check Answer</button>
                <div class="mc-feedback" style="margin-top: 0.4rem; font-weight: bold;"></div>
            </div>\n'''

    reading_html = f'''
        <!-- SECTION 5: READING COMPREHENSION -->
        <section class="section-wrapper" id="reading-section-{u_num}">
            <span class="section-label reading">📖 Section 5: Reading Comprehension</span>
            <h2 class="section-title">{reading_title}</h2>
            <div class="reading-passage" style="background: #fffdfa; border: 1px solid #fed7aa; padding: 1.2rem; border-radius: 10px; margin-bottom: 1.5rem;">
                <p style="line-height: 1.7; font-size: 1.05rem;">{reading_text}</p>
                <button class="audio-btn small" onclick="speakText('{reading_text.replace("'", "\\'")}')" style="margin-top: 0.8rem;">🔊 Listen to Reading Passage</button>
            </div>
            
            <h3 style="color:var(--accent-indigo); margin-bottom: 1rem;">Comprehension Questions (15 Items)</h3>
            {reading_items_html}
        </section>
'''

    writing_items_html = ""
    for idx, (q_text, opts, correct_val) in enumerate(writing_items, 1):
        q_id = f"u{u_num}_w_q{idx}"
        opts_html = "".join([f'<option value="{opt}">{opt}</option>' for opt in opts])
        writing_items_html += f'''                <div class="exercise-item exercise-question" data-question="{q_id}" style="margin-bottom:1rem;">
                    <p style="margin-bottom:0.4rem;"><strong>{idx}.</strong> {q_text}</p>
                    <div class="exercise-dropdown" style="display:flex; gap:0.5rem; align-items:center;">
                        <select data-correct="{correct_val}" style="padding:0.4rem 0.8rem; border-radius:6px; border:1px solid #cbd5e1;">
                            <option value="">-- Select --</option>
                            {opts_html}
                        </select>
                        <button class="check-answer-btn" onclick="checkDropdownAnswer('{q_id}')" style="padding:0.4rem 0.8rem; background:var(--accent-indigo); color:white; border:none; border-radius:6px; cursor:pointer;">Check</button>
                    </div>
                    <div class="feedback-message" style="margin-top:0.3rem; font-weight:bold;"></div>
                </div>\n'''

    writing_html = f'''
        <!-- SECTION 6: GRAMMAR & WRITING -->
        <section class="section-wrapper" id="writing-section-{u_num}">
            <span class="section-label writing">✏️ Section 6: Grammar & Writing Quiz</span>
            <h2 class="section-title">{writing_title} (15 Items)</h2>
            <div class="exercise-box">
                {writing_items_html}
            </div>
        </section>
'''

    quiz_items_html = ""
    for idx, (q_text, opts, correct_idx, expl) in enumerate(quiz_items, 1):
        q_name = f"u{u_num}_quiz_q{idx}"
        opts_divs = ""
        for o_idx, opt in enumerate(opts):
            is_cor = "true" if o_idx == correct_idx else "false"
            opts_divs += f'''                    <div class="mc-option" style="margin: 0.3rem 0; padding: 0.4rem 0.8rem; border: 1px solid #cbd5e1; border-radius: 6px;">
                        <label style="cursor: pointer; display: flex; align-items: center; gap: 0.5rem;">
                            <input type="radio" name="{q_name}" data-correct="{is_cor}"> {opt}
                        </label>
                    </div>\n'''
        
        quiz_items_html += f'''            <div class="mc-exercise" style="background: white; padding: 1rem; border-radius: 8px; margin-bottom: 1rem; box-shadow: 0 2px 4px rgba(0,0,0,0.04);">
                <p style="margin-bottom: 0.5rem; font-weight: 500;"><strong>Question {idx}:</strong> {q_text}</p>
                {opts_divs}
                <button class="mc-check-btn" onclick="checkMC('{q_name}')" style="margin-top: 0.5rem; padding: 0.3rem 0.8rem; background: var(--accent-indigo); color: white; border: none; border-radius: 6px; cursor: pointer;">Check Answer</button>
                <div class="mc-feedback" style="margin-top: 0.4rem; font-weight: bold;"></div>
                <div style="font-size: 0.85rem; color: #64748b; margin-top: 0.4rem;">💡 <em>Note: {expl}</em></div>
            </div>\n'''

    quiz_html = f'''
        <!-- SECTION 7: FINAL REVIEW QUIZ -->
        <section class="section-wrapper" id="quiz-section-{u_num}">
            <span class="section-label quiz">🏆 Section 7: Vocabulary & Grammar Check</span>
            <h2 class="section-title">{quiz_title} (15 Items)</h2>
            {quiz_items_html}
        </section>
'''

    full_unit = f'''<div id="unit-{u_num}" class="course-unit" style="display: none;">
<div class="container">
{culture_html}
{vocab_html}
{grammar_html}
{listening_html}
{oral_html}
{reading_html}
{writing_html}
{quiz_html}
</div>
</div>'''
    return full_unit
