"""Apply editorial corrections to exported Stitch HTML; safe to rerun."""
from pathlib import Path
import re

replacements = {
    'Phone Simulator • Companion bridge active': 'Demo state • Waiting for phone',
    'Your baseline fitness never vanished while you were living life.': 'Your previous logs are still here. Choose a manageable next step.',
    'Auto-balance remaining week into 3 compact sessions.': 'Preview the next feasible slot after checking availability and recovery spacing.',
    'Encrypted Cloud Health Summary Sharing': 'Optional Cloud Health Summary Sharing',
    'Zero-knowledge cryptographic snapshot shared strictly with designated recovery clinician. Decryption keys never leave this workstation.': 'Upload only consented summaries to your account. Provider encryption is not end-to-end encryption; authorized processors can access cloud data.',
    'ED25519': 'OPT-IN',
    'Key Fingerprint': 'Sharing status',
    '9E2B:4FA1:88CD:703E:AA12:0048:F99C': 'Demo only • No connection',
    'READ ONLY': 'PHONE PERMISSIONS',
    'Reads passive sensor baselines (active burn &amp; step counts). Strictly does <strong>NOT</strong> upload workout notes, custom routines, or nutritional logs back to external health ecosystems.': 'HealthKit permissions are managed on iPhone. The Watch owns its recorded workout; the phone links it without writing a duplicate. Cloud sharing is separate.',
    'Outbound Blocked': 'No live HealthKit connection',
    'EPHEMERAL RAM': 'SEPARATE OPT-IN',
    'On-demand visual nutritional decomposition. Raw photos are discarded immediately post-inference; zero model training retention agreement in effect.': 'Optional photo estimates require processor-specific consent. Review retention terms before enabling; manual food logging remains available.',
    'SQLite Encrypted': 'IndexedDB • Planned',
    'Local SQLite Engine Autonomous': 'Local browser storage • Planned',
    'Local SQLite': 'IndexedDB',
    'v3.42.0': 'Design only',
    'SQLCipher AES-256': 'Browser storage; no E2EE claim',
    'Encrypted at Rest': 'Synthetic storage example',
    'Max 2 / Day': 'Max 3 / Day',
    '2 (Recommended)': '2 Gentle Cues',
    '3 Moderate': '3 (Default)',
    'Zero Push After 8:00 PM': 'Quiet Hours 22:00–08:00',
    'Prevents bedtime cortisol spikes &amp; guilt spirals': 'Asia/Kolkata example • Respect OS Focus and permissions',
    'Last-Write-Wins with Merge Prompt': 'Revision check; preserve both conflict copies',
    '100% Offline Capable': 'Offline behavior planned',
    'Zero roundtrip dependency': 'No live sync in this prototype',
    'SQLite File': 'CSV Export',
    'Decrypted raw tables': 'Records, units and timestamps',
    'Markdown Diary': 'Account Deletion',
    'Obsidian &amp; Logseq notes': 'Preview scope and confirm',
    'Emergency Local Wipe &amp; Reset': 'Account &amp; Local Data Deletion',
    'Permanently purges local cryptographic keys, clears SQLite tables, and purges all offline cache. Irreversible without an exported vault file.': 'Review cloud records and local caches before confirming. Offline devices reconcile deletion on next contact; backup aging must be disclosed.',
    'Initiate Two-Step Vault Purge': 'Review Deletion Scope',
    'Source: Verified Home Recipe (Cooked-Yield)': 'Source: Synthetic Recipe Example (Cooked-Yield)',
    '1 Standard Katori (Indian Bowl)': 'Your Saved Katori Size (Example)',
    'true katori calories accurately': 'estimated nutrition for your measured serving',
    'Narrow variance (±35 kcal) because dal cooked-weight expansion ratio is pre-measured.': 'Illustrative range only. Ingredient values, retained fat and serving mass remain uncertain.',
    '3.0x Yield Expansion': 'Example Yield Ratio: 3.0x',
    'exactly <strong>1.05 kcal/g cooked</strong>': 'approximately <strong>1.05 kcal/g cooked (example)</strong>',
    'High capture validity for progressive adaptations.': 'Incomplete intake; no target adjustment from this example.',
    'ADHD Logging Tolerance: High': 'Logging completeness matters',
    '68% meal capture is statistically robust for lean mass retention — no need to log every condiment or bite. Perfect tracking induces burnout; rough anchors preserve consistency.': 'This example has missing meals. Missing entries do not prove low intake. Review completeness before estimating expenditure or changing targets.',
    '100% Neuro-friendly': 'No streak penalties',
    'guaranteeing that temporary life interruptions never deduct from earned physical capacity.': 'without treating missing logs as proof of either training or rest.',
    'Baseline stimulus preserved.': 'Missing observations remain unknown.',
    'Life / Rest Gap (No Data Logged)': 'No Data Logged (Activity Unknown)',
    'Target: 110-130g': 'Example only: 110–130g',
    '1 All-out Set • Low spoon day': '1 manageable set • Effort adjustable',
    '2 RIR (Optimal)': '2 RIR (2 reps left)',
    'Hypertrophy Sweet Spot': 'About 2 Reps Remaining',
    'Maximum stimulus with sustainable recovery curve.': 'An estimate of effort, not a guaranteed optimum.',
    'same motor recruitment': 'a similar movement pattern',
    'Uncompleted target sets carry forward without streak penalties.': 'Uncompleted sets remain in history; they are never automatically added to the next workout.',
    'Auto-scales based on warm-up velocity': 'Changes require review and confirmation',
    'Core stimulus threshold achieved. The remaining sessions are additive, not mandatory.': 'Two example sessions logged. Modified completion does not imply equivalent training volume.',
    'Missed workouts never roll forward or compress into double-sessions. If you skip, the volume dissipates cleanly.': 'Missed sessions need a check-in. Preview Move, Minimum or Recovery without stacking hard sessions; keep original history.',
    'Momentum discards unfulfilled days at midnight Sunday, ensuring you always begin Monday with a pristine, unburdened board.': 'Momentum preserves planned intent and completed history. Changes are proposed for review, with Undo and recovery-spacing checks.',
    'v2.4.19-local': 'Design milestone v0.1',
    'v2.4 Desktop Safe': 'Design milestone v0.1',
    'v2.4-Preview': 'v0.1-design',
    'v2.4 (Desktop Web)': 'v0.1-design (Desktop Web)',
}

root = Path(__file__).resolve().parents[1]
for path in sorted((root / 'design').glob('*/*.html')):
    source = path.read_text(encoding='utf-8')
    for old, new in replacements.items():
        source = source.replace(old, new)
    # Existing DEMO badges and concept footers identify the screens; do not overlay navigation.
    source = re.sub(r'<div role="note"[^>]*>Reviewed static concept.*?</div>', '', source)
    path.write_text(source, encoding='utf-8')
print('Reviewed exported HTML copy; all files remain static design concepts.')
