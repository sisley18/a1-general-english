// ============================================================
// A1 General English Coursebook — Audio & Interactive Script
// Web Speech API — works on ALL devices, no external requests
// ============================================================

// ============================================================
// Universal Audio Engine — Google TTS + Fallback
// Pronunciación americana garantizada y fluida en todos los dispositivos
// ============================================================
let audioQueue = [];
let isPlaying = false;
let currentAudioElement = null;
let voices = [];

function initAudioEngine() {
    if ('speechSynthesis' in window) {
        voices = window.speechSynthesis.getVoices();
        window.speechSynthesis.onvoiceschanged = () => { voices = window.speechSynthesis.getVoices(); };
    }
}
document.addEventListener('DOMContentLoaded', initAudioEngine);

function speakText(textIdOrText, slow, gender = 'female') {
    let text = document.getElementById(textIdOrText) ? (document.getElementById(textIdOrText).textContent || document.getElementById(textIdOrText).innerText) : textIdOrText;
    text = (text || '').trim();
    if (!text) return;

    text = text.replace(/[\u2018\u2019]/g, "'").replace(/[\u201C\u201D]/g, '"').replace(/\n/g, '. ').trim();
    stopAudio();

    // Chunk text for Google TTS limit (approx 200 chars max)
    const chunks = _splitText(text, 150);
    audioQueue = chunks.map(c => ({ text: c, slow: slow, gender: gender }));
    _processQueue();
}

function speakMaleText(textIdOrText, slow) {
    speakText(textIdOrText, slow, 'male');
}

function _processQueue() {
    if (audioQueue.length === 0) {
        isPlaying = false;
        return;
    }
    isPlaying = true;
    const item = audioQueue.shift();
    
    // If male voice requested, skip Google Translate TTS (which is female) and use fallback Web Speech API directly
    if (item.gender === 'male') {
        _fallbackSpeak(item.text, item.slow, 'male');
        return;
    }
    
    // Use Google Translate TTS for guaranteed high-quality American English
    const url = 'https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=en-US&q=' + encodeURIComponent(item.text);
    const audio = new Audio(url);
    
    // Slow down playback if needed
    if (item.slow) {
        audio.playbackRate = 0.75;
        audio.preservesPitch = true;
    }
    
    currentAudioElement = audio;
    
    audio.onended = () => {
        setTimeout(_processQueue, 250); // Natural pause between chunks
    };
    
    audio.onerror = () => {
        console.warn("Google TTS failed, falling back to Web Speech API");
        _fallbackSpeak(item.text, item.slow, 'female');
    };
    
    audio.play().catch(e => {
        console.warn("Audio play blocked or failed, falling back to Web Speech API", e);
        _fallbackSpeak(item.text, item.slow, 'female');
    });
}

function stopAudio() {
    audioQueue = [];
    isPlaying = false;
    if (currentAudioElement) {
        currentAudioElement.pause();
        currentAudioElement.currentTime = 0;
        currentAudioElement = null;
    }
    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
    }
}

function pauseSpeech() {
    stopAudio();
}

function speakTextSlow(text) {
    speakText(text, true);
}

// Fallback logic for Web Speech API
function _fallbackSpeak(text, slow, gender = 'female') {
    if (!('speechSynthesis' in window)) {
        setTimeout(_processQueue, 300);
        return;
    }
    const u = new SpeechSynthesisUtterance(text);
    u.lang = 'en-US';
    u.rate = slow ? 0.7 : 0.95;
    
    if (voices.length === 0) voices = window.speechSynthesis.getVoices();
    
    let selectedVoice = null;
    if (gender === 'male') {
        selectedVoice = voices.find(v => v.lang.toLowerCase().startsWith('en-us') && (v.name.toLowerCase().includes('male') || v.name.toLowerCase().includes('david') || v.name.toLowerCase().includes('guy')));
        if (!selectedVoice) selectedVoice = voices.find(v => v.lang.toLowerCase().startsWith('en') && v.name.toLowerCase().includes('male'));
    } else {
        selectedVoice = voices.find(v => v.lang.toLowerCase().startsWith('en-us') && (v.name.includes('Google') || v.name.includes('Online') || v.name.includes('Premium') || v.name.toLowerCase().includes('female') || v.name.toLowerCase().includes('zira')));
    }
    
    if (selectedVoice) {
        u.voice = selectedVoice;
    } else {
        const anyEng = voices.find(v => v.lang.toLowerCase().startsWith('en'));
        if (anyEng) u.voice = anyEng;
    }
    
    u.onend = () => { setTimeout(_processQueue, 300); };
    u.onerror = () => { setTimeout(_processQueue, 300); };
    
    window.speechSynthesis.speak(u);
}

function _splitText(text, maxLen) {
    const chunks = [];
    let remaining = text;
    while (remaining.length > 0) {
        if (remaining.length <= maxLen) { chunks.push(remaining); break; }
        let idx = remaining.lastIndexOf('. ', maxLen);
        if (idx < 0) idx = remaining.lastIndexOf('? ', maxLen);
        if (idx < 0) idx = remaining.lastIndexOf('! ', maxLen);
        if (idx < 0) idx = remaining.lastIndexOf(', ', maxLen);
        if (idx < 0) idx = remaining.lastIndexOf(' ', maxLen);
        if (idx < 0) idx = maxLen;
        chunks.push(remaining.substring(0, idx + 1).trim());
        remaining = remaining.substring(idx + 1).trim();
    }
    return chunks;
}

// --- NOTIFICATION SYSTEM ---
function showNotification(message, type) {
    var existing = document.querySelector('.notification');
    if (existing) existing.remove();

    var notif = document.createElement('div');
    notif.className = 'notification ' + (type || 'info');
    notif.textContent = message;
    document.body.appendChild(notif);

    setTimeout(function() {
        notif.style.transition = 'opacity 0.4s ease';
        notif.style.opacity = '0';
        setTimeout(function() { notif.remove(); }, 400);
    }, 3000);
}

// --- DROPDOWN NAVIGATION ---
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.dropdown').forEach(function (dropdown) {
        var btn = dropdown.querySelector('.dropdown-btn');
        var content = dropdown.querySelector('.dropdown-content');

        if (btn && content) {
            btn.addEventListener('click', function (e) {
                e.stopPropagation();
                document.querySelectorAll('.dropdown-content').forEach(function (dc) {
                    if (dc !== content) dc.style.display = 'none';
                });
                content.style.display = content.style.display === 'block' ? 'none' : 'block';
            });
        }
    });

    document.addEventListener('click', function () {
        document.querySelectorAll('.dropdown-content').forEach(function (dc) {
            dc.style.display = 'none';
        });
    });
});

// --- INTERACTIVE EXERCISE FUNCTIONS ---
function checkDropdownAnswer(questionId) {
    var container = document.querySelector('[data-question="' + questionId + '"]');
    if (!container) return;

    var select = container.querySelector('.exercise-dropdown select');
    var feedback = container.querySelector('.feedback-message');
    if (!select || !feedback) return;

    var correct = select.getAttribute('data-correct');
    var selected = select.value;

    if (!selected) {
        feedback.textContent = '⚠️ Please select an answer.';
        feedback.className = 'feedback-message incorrect';
        return;
    }

    if (selected === correct) {
        feedback.textContent = '✅ Correct! Well done!';
        feedback.className = 'feedback-message correct';
        select.style.borderColor = '#059669';
    } else {
        feedback.textContent = '❌ Try again! The correct answer is: ' + correct;
        feedback.className = 'feedback-message incorrect';
        select.style.borderColor = '#ef4444';
    }
    
    // Disable the select element so they can only answer once
    select.disabled = true;
    var checkBtn = container.querySelector('.check-answer-btn');
    if(checkBtn) checkBtn.disabled = true;
}

function checkAllExercises() {
    document.querySelectorAll('.exercise-question').forEach(function (q) {
        var id = q.getAttribute('data-question');
        if (id) checkDropdownAnswer(id);
    });
}

function resetAllExercises() {
    document.querySelectorAll('.exercise-question').forEach(function (q) {
        var select = q.querySelector('select');
        var feedback = q.querySelector('.feedback-message');
        if (select) {
            select.selectedIndex = 0;
            select.style.borderColor = '#e2e8f0';
        }
        if (feedback) {
            feedback.textContent = '';
            feedback.className = 'feedback-message';
        }
    });
}

// --- EXPORT & COPY FUNCTIONS ---
function copyClassContent() {
    var main = document.querySelector('main') || document.querySelector('.container');
    if (main) {
        navigator.clipboard.writeText(main.innerText).then(function () {
            showNotification('📋 Content copied!', 'success');
        });
    }
}

function copyVocabularySection() {
    var section = document.getElementById('vocabulary-section');
    if (section) navigator.clipboard.writeText(section.innerText);
}

function copyListeningSection() {
    var section = document.getElementById('listening-section');
    if (section) navigator.clipboard.writeText(section.innerText);
}

function copyPracticeSection() {
    var section = document.getElementById('practice-section');
    if (section) navigator.clipboard.writeText(section.innerText);
}

function exportCompleteClass() {
    var main = document.querySelector('main');
    if (!main) return;
    var title = document.title || 'A1 English Course';
    var content = main.innerHTML;
    var htmlContent = '<html><head><meta charset="utf-8"><title>' + title + '</title><style>body{font-family:Arial,sans-serif;line-height:1.6;margin:2cm;color:#333;}h1,h2,h3{color:#5a3fd6;}table{border-collapse:collapse;width:100%;}td,th{border:1px solid #ddd;padding:8px;}.vocab-card{border:1px solid #ddd;padding:1rem;margin:0.5rem 0;}</style></head><body><h1>' + title + '</h1>' + content + '</body></html>';
    var blob = new Blob(['\ufeff' + htmlContent], { type: 'application/msword' });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = title.replace(/[^a-z0-9]/gi, '_') + '.doc';
    a.click();
    URL.revokeObjectURL(url);
}

function printSection(sectionId) {
    var section = document.getElementById(sectionId) || document.querySelector('main');
    if (section) {
        var printWin = window.open('', '_blank');
        printWin.document.write('<html><head><title>Print</title><style>body{font-family:Arial,sans-serif;line-height:1.6;margin:2cm;}h1,h2,h3{color:#333;}.vocab-card{border:1px solid #ddd;padding:1rem;margin:0.5rem 0;}</style></head><body>' + section.innerHTML + '</body></html>');
        printWin.document.close();
        printWin.print();
    }
}

// --- EXPOSE FUNCTIONS GLOBALLY ---
window.speakText = speakText;
window.speakMaleText = speakMaleText;
window.speakTextSlow = speakTextSlow;
window.stopAudio = stopAudio;
window.pauseSpeech = pauseSpeech;
window.checkDropdownAnswer = checkDropdownAnswer;
window.checkAllExercises = checkAllExercises;
window.resetAllExercises = resetAllExercises;
window.copyClassContent = copyClassContent;
window.copyVocabularySection = copyVocabularySection;
window.copyListeningSection = copyListeningSection;
window.copyPracticeSection = copyPracticeSection;
window.exportCompleteClass = exportCompleteClass;
window.printSection = printSection;
window.showNotification = showNotification;

// --- MULTIPLE CHOICE EXERCISE FUNCTIONS ---
function checkMC(questionName) {
    var radios = document.querySelectorAll('input[name="' + questionName + '"]');
    if (!radios.length) return;

    var selected = null;
    radios.forEach(function(r) { if (r.checked) selected = r; });

    // Find the mc-exercise container
    var container = radios[0].closest('.mc-exercise');
    if (!container) return;
    var feedback = container.querySelector('.mc-feedback');

    if (!selected) {
        if (feedback) {
            feedback.textContent = '⚠️ Please select an answer.';
            feedback.className = 'mc-feedback show incorrect';
        }
        return;
    }

    var isCorrect = selected.getAttribute('data-correct') === 'true';

    // Reset all option styles in this question
    container.querySelectorAll('.mc-option').forEach(function(opt) {
        opt.classList.remove('correct', 'incorrect');
    });

    // Highlight correct and selected
    radios.forEach(function(r) {
        var optDiv = r.closest('.mc-option');
        if (r.getAttribute('data-correct') === 'true') {
            optDiv.classList.add('correct');
        }
        if (r === selected && !isCorrect) {
            optDiv.classList.add('incorrect');
        }
        r.disabled = true; // Disable radio button so they can only answer once
    });
    
    var checkBtn = container.querySelector('.mc-check-btn');
    if(checkBtn) checkBtn.disabled = true;

    if (feedback) {
        if (isCorrect) {
            feedback.textContent = '✅ Correct! Well done!';
            feedback.className = 'mc-feedback show correct';
        } else {
            feedback.textContent = '❌ Not quite. The correct answer is highlighted in green.';
            feedback.className = 'mc-feedback show incorrect';
        }
    }
}

function checkAllMC(sectionId) {
    var section = document.getElementById(sectionId);
    if (!section) {
        // Fallback: check all MC on the page
        document.querySelectorAll('.mc-exercise').forEach(function(ex) {
            var radio = ex.querySelector('input[type="radio"]');
            if (radio) checkMC(radio.name);
        });
        return;
    }
    section.querySelectorAll('.mc-exercise').forEach(function(ex) {
        var radio = ex.querySelector('input[type="radio"]');
        if (radio) checkMC(radio.name);
    });
}

function resetAllMC(sectionId) {
    var section = document.getElementById(sectionId);
    if (!section) {
        section = document;
    }
    section.querySelectorAll('.mc-exercise').forEach(function(ex) {
        ex.querySelectorAll('input[type="radio"]').forEach(function(r) {
            r.checked = false;
        });
        ex.querySelectorAll('.mc-option').forEach(function(opt) {
            opt.classList.remove('correct', 'incorrect');
        });
        var fb = ex.querySelector('.mc-feedback');
        if (fb) {
            fb.textContent = '';
            fb.className = 'mc-feedback';
        }
    });
}

window.checkMC = checkMC;
window.checkAllMC = checkAllMC;
window.resetAllMC = resetAllMC;

// --- FILL IN THE BLANKS & SEND TO TEACHER ---
document.addEventListener('DOMContentLoaded', function () {
    var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
    var nodesToReplace = [];
    while (walker.nextNode()) {
        var node = walker.currentNode;
        if (node.nodeValue.match(/_{3,}/)) {
            nodesToReplace.push(node);
        }
    }
    
    if (nodesToReplace.length > 0 || document.querySelectorAll('textarea').length > 0) {
        nodesToReplace.forEach(function(node) {
            var span = document.createElement('span');
            var replacedText = node.nodeValue.replace(/_{3,}/g, '<input type="text" class="fill-in-blank-input" placeholder="✏️" style="border:none; border-bottom: 2px solid #5a3fd6; background:rgba(255,255,255,0.1); color:inherit; font-family:inherit; font-size:1rem; width:100px; text-align:center; outline:none; margin: 0 5px; padding: 2px;">');
            span.innerHTML = replacedText;
            node.parentNode.replaceChild(span, node);
        });

        // Email Button (Gmail)
        var sendBtn = document.createElement('button');
        sendBtn.innerHTML = '📧 Send via Gmail';
        sendBtn.className = 'send-teacher-btn';
        sendBtn.style.cssText = 'position:fixed; bottom:20px; right:20px; background:linear-gradient(135deg,#db2777,#9d174d); color:white; border:none; padding:15px 25px; border-radius:30px; font-weight:bold; font-size:1rem; cursor:pointer; box-shadow:0 10px 25px rgba(0,0,0,0.3); z-index:9999; transition: transform 0.2s;';
        sendBtn.onmouseover = function() { sendBtn.style.transform = 'scale(1.05)'; };
        sendBtn.onmouseout = function() { sendBtn.style.transform = 'scale(1)'; };
        sendBtn.onclick = sendToTeacher;
        document.body.appendChild(sendBtn);

        // WhatsApp Button
        var waBtn = document.createElement('button');
        waBtn.innerHTML = '📱 Send via WhatsApp';
        waBtn.className = 'send-teacher-wa-btn';
        waBtn.style.cssText = 'position:fixed; bottom:80px; right:20px; background:linear-gradient(135deg,#25D366,#128C7E); color:white; border:none; padding:15px 25px; border-radius:30px; font-weight:bold; font-size:1rem; cursor:pointer; box-shadow:0 10px 25px rgba(0,0,0,0.3); z-index:9999; transition: transform 0.2s;';
        waBtn.onmouseover = function() { waBtn.style.transform = 'scale(1.05)'; };
        waBtn.onmouseout = function() { waBtn.style.transform = 'scale(1)'; };
        waBtn.onclick = sendToTeacherWhatsApp;
        document.body.appendChild(waBtn);
    }
});

function getAnswersText() {
    var answers = [];
    var inputs = document.querySelectorAll('.fill-in-blank-input');
    inputs.forEach(function(input, index) {
        answers.push('Blank ' + (index + 1) + ': ' + (input.value || '(empty)'));
    });
    
    var textareas = document.querySelectorAll('textarea');
    textareas.forEach(function(ta, index) {
        answers.push('Open Question ' + (index + 1) + ': ' + (ta.value || '(empty)'));
    });
    return answers;
}

function sendToTeacher() {
    var answers = getAnswersText();
    if(answers.length === 0) {
        showNotification('No answers found!', 'info');
        return;
    }

    var bodyText = 'Hello Teacher,\n\nHere are my answers:\n\n' + answers.join('\n') + '\n\nBest regards.';
    var gmailLink = 'https://mail.google.com/mail/?view=cm&fs=1&su=' + encodeURIComponent('My English Exercises') + '&body=' + encodeURIComponent(bodyText);
    
    window.open(gmailLink, '_blank');
    showNotification('📧 Opening Gmail to send your answers...', 'success');
}

function sendToTeacherWhatsApp() {
    var answers = getAnswersText();
    if(answers.length === 0) {
        showNotification('No answers found!', 'info');
        return;
    }

    var bodyText = 'Hello Teacher, here are my answers:\n\n' + answers.join('\n');
    var waLink = 'https://wa.me/?text=' + encodeURIComponent(bodyText);
    
    window.open(waLink, '_blank');
    showNotification('📱 Opening WhatsApp...', 'success');
}

window.sendToTeacher = sendToTeacher;
window.sendToTeacherWhatsApp = sendToTeacherWhatsApp;

// --- SINGLE PAGE APPLICATION NAVIGATION ---
let currentUnit = 0;
const totalUnits = 24;

function navigateUnitTo(unitNum) {
    document.querySelectorAll('.course-unit').forEach(el => el.style.display = 'none');
    const target = document.getElementById('unit-' + unitNum);
    if(target) target.style.display = 'block';
    currentUnit = unitNum;
    
    const display = document.getElementById('current-unit-display');
    if(display) {
        display.innerText = unitNum === 0 ? 'Home' : 'Unit ' + unitNum;
    }
    window.scrollTo(0, 0);
}

function navigateUnit(dir) {
    let nextUnit = currentUnit + dir;
    if(nextUnit < 0) nextUnit = 0;
    if(nextUnit > totalUnits) nextUnit = totalUnits;
    
    // Skip deleted units 1-4
    if (nextUnit >= 1 && nextUnit <= 4) {
        if (dir > 0) {
            nextUnit = 5;
        } else {
            nextUnit = 0;
        }
    }
    
    navigateUnitTo(nextUnit);
}

window.navigateUnitTo = navigateUnitTo;
window.navigateUnit = navigateUnit;


