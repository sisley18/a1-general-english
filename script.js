// ============================================================
// A1 General English Coursebook — Audio & Interactive Script
// Web Speech API — works on ALL devices, no external requests
// ============================================================

// Pre-load voices robustly
let availableVoices = [];
function initVoices() {
    availableVoices = window.speechSynthesis.getVoices();
}
if (window.speechSynthesis) {
    initVoices();
    window.speechSynthesis.onvoiceschanged = initVoices;
}

function speakText(textIdOrText, slow) {
    if (!window.speechSynthesis) return;
    window.speechSynthesis.cancel();

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

    var doSpeak = function() {
        var utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'en-US';
        utterance.rate = slow ? 0.7 : 0.95; // Slightly faster default to sound less robotic
        utterance.pitch = 1.0;

        if (availableVoices.length === 0) availableVoices = window.speechSynthesis.getVoices();

        var voice =
            availableVoices.find(function(v) { return v.name.includes('Google US English') || v.name.includes('Google') && v.lang === 'en-US'; }) ||
            availableVoices.find(function(v) { return v.name.includes('Microsoft Zira') || v.name.includes('Microsoft David') || v.name.includes('Microsoft Mark'); }) ||
            availableVoices.find(function(v) { return v.name === 'Samantha' || v.name === 'Alex' || v.name === 'Victoria'; }) ||
            availableVoices.find(function(v) { return v.lang === 'en-US' && v.localService; }) ||
            availableVoices.find(function(v) { return v.lang === 'en-US'; }) ||
            availableVoices.find(function(v) { return v.lang && v.lang.indexOf('en') === 0; });

        if (voice) {
            utterance.voice = voice;
        }

        utterance.onerror = function(e) {
            if (e.error !== 'interrupted' && e.error !== 'canceled') {
                console.error('Speech error:', e.error);
            }
        };

        window.speechSynthesis.speak(utterance);
    };

    if (availableVoices.length === 0) {
        setTimeout(doSpeak, 50);
    } else {
        doSpeak();
    }
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
