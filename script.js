// ============================================================
// A1 General English Coursebook — Audio & Interactive Script
// Web Speech API — works on ALL devices, no external requests
// ============================================================

// Pre-load voices
if (window.speechSynthesis) {
    window.speechSynthesis.getVoices();
    window.speechSynthesis.onvoiceschanged = function() {
        window.speechSynthesis.getVoices();
    };
}

function speakText(textIdOrText, slow) {
    if (window.speechSynthesis) window.speechSynthesis.cancel();

    var text;
    var el = document.getElementById(textIdOrText);
    if (el) {
        text = el.textContent || el.innerText;
    } else {
        text = textIdOrText;
    }
    text = (text || '').trim();
    if (!text) return;

    text = text.replace(/[\u2018\u2019]/g, "'").replace(/[\u201C\u201D]/g, '"').replace(/\n/g, '. ').trim();

    var utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'en-US';
    utterance.rate = slow ? 0.6 : 0.9;
    utterance.pitch = 1.0;

    var voices = window.speechSynthesis.getVoices();
    var voice =
        voices.find(function(v){ return v.name === 'Google US English'; }) ||
        voices.find(function(v){ return v.name === 'Samantha'; }) ||
        voices.find(function(v){ return v.name === 'Alex'; }) ||
        voices.find(function(v){ return v.lang === 'en-US'; }) ||
        voices.find(function(v){ return v.lang && v.lang.indexOf('en') === 0; });

    if (voice) utterance.voice = voice;

    utterance.onerror = function(e) {
        if (e.error !== 'interrupted' && e.error !== 'canceled') {
            console.error('Speech error:', e.error);
        }
    };

    window.speechSynthesis.speak(utterance);
}

function speakTextSlow(textIdOrText) {
    speakText(textIdOrText, true);
}

function stopAudio() {
    if (window.speechSynthesis) window.speechSynthesis.cancel();
}

function pauseSpeech() {
    stopAudio();
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
