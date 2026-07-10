// ============================================================
// A1 General English Coursebook — Audio & Interactive Script
// Uses Google Neural TTS for professional American pronunciation
// ============================================================

// --- AUDIO ENGINE: Web Speech API ---
// Uses native speech synthesis for 100% reliable playback on all devices (bypasses iOS autoplay blocks)
let currentUtterance = null;

/**
 * Ensures voices are loaded (some browsers load them asynchronously)
 */
function getVoices() {
    return new Promise(resolve => {
        let voices = window.speechSynthesis.getVoices();
        if (voices.length) {
            resolve(voices);
            return;
        }
        window.speechSynthesis.onvoiceschanged = () => {
            voices = window.speechSynthesis.getVoices();
            resolve(voices);
        };
    });
}

/**
 * Plays text using Web Speech API with American English.
 */
async function speakText(textIdOrText, slow = false) {
    stopAudio();

    if (!window.speechSynthesis) {
        showNotification('Audio not supported on this device', 'error');
        return;
    }

    let text;
    const el = document.getElementById(textIdOrText);
    if (el) {
        text = el.textContent || el.innerText;
    } else {
        text = textIdOrText;
    }

    text = text.trim();
    if (!text) {
        showNotification('No text to read', 'error');
        return;
    }

    // Clean text
    text = text.replace(/\u2018|\u2019/g, "'").replace(/\u201C|\u201D/g, '"').replace(/\u2013/g, '-').replace(/\n/g, '. ').trim();

    currentUtterance = new SpeechSynthesisUtterance(text);
    currentUtterance.lang = 'en-US'; // Force American English
    currentUtterance.rate = slow ? 0.65 : 0.95; // Natural speed
    currentUtterance.pitch = 1.0;

    const voices = await getVoices();
    // Prioritize natural sounding US English voices
    const selectedVoice = 
        voices.find(v => v.name === 'Google US English') ||
        voices.find(v => v.name === 'Samantha') ||
        voices.find(v => v.name === 'Alex') ||
        voices.find(v => v.lang === 'en-US');

    if (selectedVoice) {
        currentUtterance.voice = selectedVoice;
    }

    currentUtterance.onstart = () => {
        // Silently start
    };
    currentUtterance.onend = () => {
        // Silently end
    };
    currentUtterance.onerror = (e) => {
        if (e.error !== 'interrupted' && e.error !== 'canceled') {
            console.error('Audio error:', e);
        }
    };

    window.speechSynthesis.speak(currentUtterance);
}

/**
 * Plays text at slow speed.
 */
function speakTextSlow(textIdOrText) {
    speakText(textIdOrText, true);
}

/**
 * Stops all audio playback.
 */
function stopAudio() {
    if (window.speechSynthesis) {
        window.speechSynthesis.cancel();
    }
    const notif = document.querySelector('.notification');
    if(notif) notif.remove();
}

// Alias for compatibility with B1 style
function pauseSpeech() {
    stopAudio();
}

// --- NOTIFICATION SYSTEM ---
function showNotification(message, type = 'info') {
    // Remove existing notification
    const existing = document.querySelector('.notification');
    if (existing) existing.remove();

    const notif = document.createElement('div');
    notif.className = `notification ${type}`;
    notif.textContent = message;
    document.body.appendChild(notif);

    setTimeout(() => {
        notif.style.transition = 'opacity 0.4s ease';
        notif.style.opacity = '0';
        setTimeout(() => notif.remove(), 400);
    }, 3000);
}

// --- DROPDOWN NAVIGATION ---
document.addEventListener('DOMContentLoaded', function () {
    // Setup all dropdowns
    document.querySelectorAll('.dropdown').forEach(function (dropdown) {
        const btn = dropdown.querySelector('.dropdown-btn');
        const content = dropdown.querySelector('.dropdown-content');

        if (btn && content) {
            btn.addEventListener('click', function (e) {
                e.stopPropagation();
                // Close other dropdowns
                document.querySelectorAll('.dropdown-content').forEach(function (dc) {
                    if (dc !== content) dc.style.display = 'none';
                });
                content.style.display = content.style.display === 'block' ? 'none' : 'block';
            });
        }
    });

    // Close dropdowns on outside click
    document.addEventListener('click', function () {
        document.querySelectorAll('.dropdown-content').forEach(function (dc) {
            dc.style.display = 'none';
        });
    });
});

// --- INTERACTIVE EXERCISE FUNCTIONS ---
function checkDropdownAnswer(questionId) {
    const container = document.querySelector(`[data-question="${questionId}"]`);
    if (!container) return;

    const select = container.querySelector('.exercise-dropdown select');
    const feedback = container.querySelector('.feedback-message');
    if (!select || !feedback) return;

    const correct = select.getAttribute('data-correct');
    const selected = select.value;

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
        const id = q.getAttribute('data-question');
        if (id) checkDropdownAnswer(id);
    });
}

function resetAllExercises() {
    document.querySelectorAll('.exercise-question').forEach(function (q) {
        const select = q.querySelector('select');
        const feedback = q.querySelector('.feedback-message');
        if (select) {
            select.selectedIndex = 0;
            select.style.borderColor = '#e2e8f0';
        }
        if (feedback) {
            feedback.textContent = '';
            feedback.className = 'feedback-message';
        }
    });
    showNotification('🔄 Quiz reset!', 'info');
}

// --- EXPORT & COPY FUNCTIONS ---
function copyClassContent() {
    const main = document.querySelector('main') || document.querySelector('.container');
    if (main) {
        const text = main.innerText;
        navigator.clipboard.writeText(text).then(function () {
            showNotification('📋 Content copied to clipboard!', 'success');
        }).catch(function () {
            showNotification('❌ Could not copy content', 'error');
        });
    }
}

function copyVocabularySection() {
    const section = document.getElementById('vocabulary-section');
    if (section) {
        navigator.clipboard.writeText(section.innerText).then(function () {
            showNotification('📚 Vocabulary copied!', 'success');
        });
    }
}

function copyListeningSection() {
    const section = document.getElementById('listening-section');
    if (section) {
        navigator.clipboard.writeText(section.innerText).then(function () {
            showNotification('🎧 Listening materials copied!', 'success');
        });
    }
}

function copyPracticeSection() {
    const section = document.getElementById('practice-section');
    if (section) {
        navigator.clipboard.writeText(section.innerText).then(function () {
            showNotification('🎯 Practice activities copied!', 'success');
        });
    }
}

function exportCompleteClass() {
    const main = document.querySelector('main');
    if (!main) return;

    const title = document.title || 'A1 English Course';
    const content = main.innerHTML;

    const htmlContent = `
        <html><head><meta charset="utf-8"><title>${title}</title>
        <style>body{font-family:Arial,sans-serif;line-height:1.6;margin:2cm;color:#333;}
        h1,h2,h3{color:#5a3fd6;}table{border-collapse:collapse;width:100%;}
        td,th{border:1px solid #ddd;padding:8px;}.vocab-card{border:1px solid #ddd;padding:1rem;margin:0.5rem 0;}
        </style></head><body><h1>${title}</h1>${content}</body></html>`;

    const blob = new Blob(['\ufeff' + htmlContent], { type: 'application/msword' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = title.replace(/[^a-z0-9]/gi, '_') + '.doc';
    a.click();
    URL.revokeObjectURL(url);
    showNotification('📄 Exported to Word!', 'success');
}

function printSection(sectionId) {
    const section = document.getElementById(sectionId) || document.querySelector('main');
    if (section) {
        const printWin = window.open('', '_blank');
        printWin.document.write(`<html><head><title>Print</title>
            <style>body{font-family:Arial,sans-serif;line-height:1.6;margin:2cm;}
            h1,h2,h3{color:#333;}.vocab-card{border:1px solid #ddd;padding:1rem;margin:0.5rem 0;}
            </style></head><body>${section.innerHTML}</body></html>`);
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
