#!/usr/bin/env node
/**
 * Simple JavaScript syntax validator
 * Checks if game.js and tracing.js are valid JavaScript
 */

const fs = require('fs');
const path = require('path');

function validateJavaScript(filePath) {
    console.log(`\n🔍 Validating: ${path.basename(filePath)}`);
    
    try {
        const code = fs.readFileSync(filePath, 'utf8');
        
        // Try to parse it (basic syntax check)
        new Function(code);
        
        console.log(`✅ Syntax valid`);
        
        // Check for common patterns
        const checks = {
            'DOM queries': code.match(/document\.getElementById/g)?.length || 0,
            'Event listeners': code.match(/addEventListener/g)?.length || 0,
            'Functions defined': code.match(/function\s+\w+\s*\(/g)?.length || 0,
            'Arrow functions': code.match(/=>\s*[{(]/g)?.length || 0,
            'const/let declarations': code.match(/\b(const|let)\s+\w+/g)?.length || 0,
        };
        
        console.log('📊 Code statistics:');
        Object.entries(checks).forEach(([name, count]) => {
            console.log(`   ${name}: ${count}`);
        });
        
        return true;
    } catch (error) {
        console.log(`❌ Syntax error: ${error.message}`);
        return false;
    }
}

function main() {
    console.log('='.repeat(60));
    console.log('🎮 JavaScript Validator');
    console.log('='.repeat(60));
    
    const files = [
        path.join(__dirname, 'game.js'),
        path.join(__dirname, 'tracing.js')
    ];
    
    let allValid = true;
    
    for (const file of files) {
        if (!fs.existsSync(file)) {
            console.log(`\n⚠️  File not found: ${file}`);
            allValid = false;
            continue;
        }
        
        if (!validateJavaScript(file)) {
            allValid = false;
        }
    }
    
    console.log('\n' + '='.repeat(60));
    if (allValid) {
        console.log('✅ All files validated successfully');
        process.exit(0);
    } else {
        console.log('❌ Validation failed');
        process.exit(1);
    }
}

main();
