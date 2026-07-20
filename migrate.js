const fs = require('fs');
const path = require('path');

const units = ['unit1.html', 'unit2.html', 'unit3.html', 'unit4.html', 'unit5.html', 'unit6.html', 'unit7.html', 'unit8.html'];

let combinedHtml = '';

units.forEach((unit, index) => {
    const unitNum = index + 1;
    if (fs.existsSync(unit)) {
        const content = fs.readFileSync(unit, 'utf8');
        
        // Extract everything inside <main>...</main>
        const mainMatch = content.match(/<main[^>]*>([\s\S]*?)<\/main>/i);
        if (mainMatch) {
            let innerContent = mainMatch[1];
            
            // Fix any local anchor links (like href="index.html") to avoid breaking SPA navigation
            innerContent = innerContent.replace(/href="index\.html"/g, 'href="#" onclick="navigateUnitTo(0); return false;"');
            
            combinedHtml += `\n<div id="unit-${unitNum}" class="course-unit" style="display: ${unitNum === 1 ? 'block' : 'none'};">\n`;
            combinedHtml += innerContent;
            combinedHtml += `\n</div>\n`;
        }
    }
});

let indexContent = fs.readFileSync('index.html', 'utf8');

// We will replace the entire <main>...</main> in index.html with our new combined layout
const newMainContent = `
    <main id="main">
        <div class="container" id="curriculum-container">
            <!-- Home Hub View -->
            <div id="unit-0" class="course-unit" style="display: block;">
                <section class="index-hero" style="text-align: center; margin-bottom: 2rem;">
                    <span class="hero-badge" style="background: rgba(99,102,241,0.1); color: #6366f1; padding: 0.5rem 1rem; border-radius: 20px; font-weight: bold;">🌟 CEFR Level A1 — Beginner</span>
                    <h1 style="font-size: 2.5rem; margin-top: 1rem;">A1 General English</h1>
                    <p style="color: #64748b; font-size: 1.1rem; max-width: 600px; margin: 1rem auto;">8 complete units with Listening, Speaking, Reading, and Writing activities.</p>
                </section>
                <div class="unit-grid" style="display: grid; gap: 1.5rem; grid-template-columns: 1fr; max-width: 600px; margin: 0 auto;">
                    <a href="#" onclick="navigateUnitTo(1); return false;" class="unit-card" style="text-align: center; text-decoration: none; padding: 2rem; border-radius: 12px; border: 1px solid #e2e8f0; background: white; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);">
                        <div class="unit-card-header">
                            <span class="unit-number" style="font-size: 2rem;">📚</span>
                            <h3 style="font-size: 1.8rem; margin: 1rem 0; color: #1e293b;">Start Course</h3>
                            <p style="font-size: 1.1rem; color: #64748b;">Complete Course (Units 1 - 8)</p>
                        </div>
                    </a>
                    
                    <a href="#" onclick="navigateUnitTo(4); setTimeout(() => { document.getElementById('progress-test').scrollIntoView(); }, 100); return false;" class="unit-card" style="text-align: center; text-decoration: none; padding: 2rem; border-radius: 12px; border: 2px solid #ef4444; background: white; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);">
                        <div class="unit-card-header" style="background: linear-gradient(135deg, #ef4444, #dc2626); color: white; padding: 1.5rem; border-radius: 8px;">
                            <span class="unit-number" style="font-size: 2.5rem;">📝</span>
                            <h3 style="font-size: 1.6rem; margin: 0.5rem 0; color: white;">Progress Test (Units 1–4)</h3>
                        </div>
                    </a>
                </div>
            </div>
            
            ${combinedHtml}
        </div>
    </main>
`;

indexContent = indexContent.replace(/<section class="index-hero">[\s\S]*?<\/section>\s*<main>[\s\S]*?<\/main>/i, newMainContent);

// Add Navigation Buttons to the Header in index.html
const navButtons = `
                <div class="spa-nav" style="display: flex; gap: 10px; align-items: center; justify-content: center; margin-top: 15px;">
                    <button class="nav-btn" onclick="navigateUnit(-1)" style="padding: 8px 16px; background: rgba(255,255,255,0.2); color: white; border: 1px solid rgba(255,255,255,0.4); border-radius: 6px; cursor: pointer; font-weight: bold;">← Previous</button>
                    <span id="current-unit-display" style="font-weight: bold; color: white; background: rgba(0,0,0,0.2); padding: 4px 12px; border-radius: 12px;">Home</span>
                    <button class="nav-btn" onclick="navigateUnit(1)" style="padding: 8px 16px; background: rgba(255,255,255,0.2); color: white; border: 1px solid rgba(255,255,255,0.4); border-radius: 6px; cursor: pointer; font-weight: bold;">Next →</button>
                </div>
`;

// Insert the nav buttons after the dropdown menu in index.html header
indexContent = indexContent.replace(/(<\/nav>)/i, `${navButtons}\n            $1`);

// Update dropdown links to use JavaScript navigation instead of page links
indexContent = indexContent.replace(/href="unit(\d+)\.html(#.*)?"/g, 'href="#" onclick="navigateUnitTo($1); return false;"');


fs.writeFileSync('index.html', indexContent);

// Delete the old unit files
units.forEach(unit => {
    if (fs.existsSync(unit)) {
        fs.unlinkSync(unit);
    }
});

console.log("Migration complete!");
