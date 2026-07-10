// ============================================================
// A1 General English Coursebook — Audio & Interactive Script
// Uses Google Neural TTS for professional American pronunciation
// ============================================================

// --- AUDIO ENGINE: Google Neural TTS ---
let currentAudio = null;
let audioQueue = [];
let isPlaying = false;

/**
 * Splits text into chunks at sentence boundaries, max ~190 chars each.
 * This ensures Google TTS returns smooth, natural audio.
 */
function splitTextIntoChunks(text, maxLen = 190) {
    const sentences = text.replace(/([.!?])\s+/g, '$1|').split('|');
    const chunks = [];
    let current = '';

    for (const sentence of sentences) {
        const trimmed = sentence.trim();
        if (!trimmed) continue;

        if (current.length + trimmed.length + 1 <= maxLen) {
            current += (current ? ' ' : '') + trimmed;
        } else {
            if (current) chunks.push(current);
            // If a single sentence exceeds maxLen, split by comma
            if (trimmed.length > maxLen) {
                const parts = trimmed.split(/,\s*/);
                let sub = '';
                for (const part of parts) {
                    if (sub.length + part.length + 2 <= maxLen) {
                        sub += (sub ? ', ' : '') + part;
                    } else {
                        if (sub) chunks.push(sub);
                        sub = part;
                    }
                }
                if (sub) current = sub;
                else current = '';
            } else {
                current = trimmed;
            }
        }
    }
    if (current) chunks.push(current);
    return chunks;
}

/**
 * Plays text using Google Neural TTS.
 * Produces clear, professional American English audio on any device.
 */
function speakText(textIdOrText, slow = false) {
    // Stop any current audio
    stopAudio();

    let text;
    // Try to get element by ID first
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

    // Clean text for TTS
    text = text
        .replace(/\u2018|\u2019/g, "'")
        .replace(/\u201C|\u201D/g, '"')
        .replace(/\u2013/g, '-')
        .replace(/\u2014/g, ' - ')
        .replace(/\n/g, '. ')
        .replace(/\.\./g, '.')
        .replace(/\s+/g, ' ')
        .trim();

    const chunks = splitTextIntoChunks(text);
    audioQueue = chunks.map(chunk => {
        const encoded = encodeURIComponent(chunk);
        let url = `https://translate.googleapis.com/translate_tts?ie=UTF-8&client=gtx&tl=en-US&q=${encoded}`;
        if (slow) {
            url += '&ttsspeed=0.24';
        }
        return url;
    });

    isPlaying = true;
    showNotification('🎧 Audio playing...', 'info');
    playNextChunk();
}

/**
 * Plays text at slow speed for practice.
 */
function speakTextSlow(textIdOrText) {
    speakText(textIdOrText, true);
}

/**
 * Plays the next chunk in the audio queue.
 */
function playNextChunk() {
    if (!isPlaying || audioQueue.length === 0) {
        isPlaying = false;
        currentAudio = null;
        if (audioQueue.length === 0) {
            showNotification('✅ Audio finished', 'success');
        }
        return;
    }

    const url = audioQueue.shift();
    currentAudio = new Audio(url);

    currentAudio.onended = function () {
        playNextChunk();
    };

    currentAudio.onerror = function () {
        console.warn('Audio chunk error, trying next...');
        playNextChunk();
    };

    currentAudio.play().catch(function (err) {
        console.error('Audio play error:', err);
        playNextChunk();
    });
}

/**
 * Stops all audio playback.
 */
function stopAudio() {
    isPlaying = false;
    audioQueue = [];
    if (currentAudio) {
        currentAudio.pause();
        currentAudio.currentTime = 0;
        currentAudio = null;
    }
    showNotification('🔇 Audio stopped', 'info');
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
