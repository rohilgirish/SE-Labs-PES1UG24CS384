import os

def create_chat_history_pdf(output_filename="chat_history.pdf"):
    # Content of the chat history
    sections = [
        ("LAB 4: VIBE CODING - LLM CHAT HISTORY & TRAJECTORY", "TITLE"),
        ("Student SRN: PES1UG24CS384", "META"),
        ("Scenario: 15 (Connect Four vs AI)", "META"),
        ("Claude Chat Share Link: https://claude.ai/share/56914cc2-0791-40fb-b8c1-a1e3acbea036", "META"),
        ("Deliverable: (c) Complete Chat History Document / PDF", "META"),
        ("", "TEXT"),
        ("1. OVERVIEW & INITIAL BUG REPRODUCTION", "HEADING"),
        ("Original Defect Identified:", "SUBHEADING"),
        ("In board.py, the winner(token) method checked only horizontal (0, 1) and vertical (1, 0)", "TEXT"),
        ("directions. Both diagonal directions (1, 1) down-right and (1, -1) down-left were omitted.", "TEXT"),
        ("Additionally, the AI in ai.py made purely random choices without detecting 1-move threats.", "TEXT"),
        ("The 'before.mp4' video was recorded demonstrating these original flaws.", "TEXT"),
        ("", "TEXT"),
        ("2. ITERATION 1: TASK 1 - COMPLETE WIN DETECTION", "HEADING"),
        ("User Prompt 1:", "SUBHEADING"),
        ("'In board.py, update the winner method to detect 4-in-a-row in all four directions: horizontal,", "PROMPT"),
        ("vertical, diagonal down-right (1, 1), and diagonal down-left (1, -1). Ensure shorter sequences", "PROMPT"),
        ("do not count as wins.'", "PROMPT"),
        ("LLM Implementation Applied in board.py:", "SUBHEADING"),
        ("    def winner(self, token):", "CODE"),
        ("        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]", "CODE"),
        ("        for r in range(ROWS):", "CODE"),
        ("            for c in range(COLS):", "CODE"),
        ("                if self.grid[r][c] != token: continue", "CODE"),
        ("                for dr, dc in directions:", "CODE"),
        ("                    if all(0 <= r + i*dr < ROWS and 0 <= c + i*dc < COLS and", "CODE"),
        ("                           self.grid[r + i*dr][c + i*dc] == token for i in range(4)):", "CODE"),
        ("                        return True", "CODE"),
        ("        return False", "CODE"),
        ("Result: Task 1 Verified & Committed (Commit: Task 1: Complete win detection).", "TEXT"),
        ("", "TEXT"),
        ("3. ITERATION 2: TASK 2 - GAME TERMINATION & INPUT VALIDATION", "HEADING"),
        ("User Prompt 2:", "SUBHEADING"),
        ("'In game.py, ensure proper input validation for column numbers (1 to 7), clean error messages", "PROMPT"),
        ("when a column is full or invalid without crashing, and ensure winning moves and draws terminate", "PROMPT"),
        ("the game cleanly.'", "PROMPT"),
        ("LLM Implementation Applied in game.py:", "SUBHEADING"),
        ("    - Added bounds checking (1 to 7) and ValueError handling for non-numeric input.", "TEXT"),
        ("    - Added clean error message when a column is already full without crashing.", "TEXT"),
        ("    - Handled 'q' and KeyboardInterrupt cleanly to exit without unhandled exceptions.", "TEXT"),
        ("    - Ensured winning moves and full board conditions terminate the game loop immediately.", "TEXT"),
        ("Result: Task 2 Verified & Committed (Commit: Task 2: Complete game termination).", "TEXT"),
        ("", "TEXT"),
        ("4. ITERATION 3: TASK 3 - INTELLIGENT AI DECISION MAKING", "HEADING"),
        ("User Prompt 3:", "SUBHEADING"),
        ("'In ai.py, upgrade the AI decision-making: first check if the AI has an immediate winning move", "PROMPT"),
        ("and take it; second check if the opponent has an immediate winning move on their next turn and", "PROMPT"),
        ("block it; otherwise choose safely from the remaining legal columns. Handle full columns safely.'", "PROMPT"),
        ("LLM Implementation Applied in ai.py:", "SUBHEADING"),
        ("    - Step 1: Simulated AI move on board copy -> takes immediate winning drop.", "TEXT"),
        ("    - Step 2: Simulated Player move on board copy -> blocks immediate 4-in-a-row threat.", "TEXT"),
        ("    - Step 3: Filters unsafe moves (moves that hand opponent a win directly above).", "TEXT"),
        ("    - Step 4: Prefers center column (col index 3) when multiple safe choices exist.", "TEXT"),
        ("Result: Task 3 Verified & Committed (Commit: Task 3: Improve AI decision making).", "TEXT"),
        ("", "TEXT"),
        ("5. ITERATION 4: TASK 4 - MOVE-LEVEL FEEDBACK", "HEADING"),
        ("User Prompt 4:", "SUBHEADING"),
        ("'In game.py, add concise move-level feedback that prints which column the player or AI", "PROMPT"),
        ("successfully placed their disc into, appearing exactly once per actual move.'", "PROMPT"),
        ("LLM Implementation Applied in game.py:", "SUBHEADING"),
        ("    who = 'You' if self.turn == 'X' else 'AI'", "CODE"),
        ("    print(f'{who} placed a disc in column {col + 1}.')", "CODE"),
        ("Result: Task 4 Verified & Committed (Commit: Task 4: Add concise move-level feedback).", "TEXT"),
        ("", "TEXT"),
        ("6. SUMMARY OF DELIVERABLES & VERIFICATION", "HEADING"),
        ("- Tasks 1-4 completed in under 4 prompt iterations.", "TEXT"),
        ("- 'before.mp4' (Original buggy/unblocked gameplay recorded).", "TEXT"),
        ("- 'after.mp4' (Updated gameplay showing feedback, smart blocking, and diagonal win).", "TEXT"),
        ("- All files pushed to personal repo: https://github.com/rohilgirish/SE-Labs-PES1UG24CS384", "TEXT"),
    ]

    # Split into pages of ~45 lines
    lines_per_page = 44
    pages_data = []
    current_page = []
    for item in sections:
        current_page.append(item)
        if len(current_page) >= lines_per_page:
            pages_data.append(current_page)
            current_page = []
    if current_page:
        pages_data.append(current_page)

    num_pages = len(pages_data)
    objects = []
    
    # 1: Catalog
    # 2: Pages object
    # For each page i (0 to num_pages-1):
    #   Page object: index = 3 + 2*i
    #   Contents object: index = 4 + 2*i
    # Font 1: index = 3 + 2*num_pages
    # Font 2 (Bold): index = 4 + 2*num_pages
    # Font 3 (Courier): index = 5 + 2*num_pages

    font_regular_id = 3 + 2 * num_pages
    font_bold_id = 4 + 2 * num_pages
    font_courier_id = 5 + 2 * num_pages

    page_obj_ids = [3 + 2 * i for i in range(num_pages)]

    # Catalog & Pages
    objects.append(b"1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj")
    kids_str = " ".join(f"{pid} 0 R" for pid in page_obj_ids)
    objects.append(f"2 0 obj << /Type /Pages /Kids [{kids_str}] /Count {num_pages} >> endobj".encode())

    for i, page_lines in enumerate(pages_data):
        page_id = 3 + 2 * i
        contents_id = 4 + 2 * i
        
        # Build stream for page
        stream_parts = ["BT"]
        # Header / Page Number
        stream_parts.append(f"/F1 9 Tf 40 810 Td (PES University - SE Labs | PES1UG24CS384) Tj 400 0 Td (Page {i+1} of {num_pages}) Tj")
        
        y_pos = 780
        stream_parts.append(f"ET BT 40 {y_pos} Td 14 TL")
        
        for text, style in page_lines:
            escaped = text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
            if style == "TITLE":
                stream_parts.append(f"/F2 14 Tf ({escaped}) ' /F1 9.5 Tf")
            elif style == "HEADING":
                stream_parts.append(f"/F2 11 Tf ({escaped}) ' /F1 9.5 Tf")
            elif style == "SUBHEADING":
                stream_parts.append(f"/F2 9.5 Tf ({escaped}) ' /F1 9.5 Tf")
            elif style == "META":
                stream_parts.append(f"/F1 9.5 Tf ({escaped}) '")
            elif style == "PROMPT":
                stream_parts.append(f"/F1 9.5 Tf (    {escaped}) '")
            elif style == "CODE":
                stream_parts.append(f"/F3 8.5 Tf ({escaped}) ' /F1 9.5 Tf")
            else:
                stream_parts.append(f"/F1 9.5 Tf ({escaped}) '")

        stream_parts.append("ET")
        stream_content = "\n".join(stream_parts).encode("latin1", "replace")

        # Page Object
        objects.append(f"{page_id} 0 obj << /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Resources << /Font << /F1 {font_regular_id} 0 R /F2 {font_bold_id} 0 R /F3 {font_courier_id} 0 R >> >> /Contents {contents_id} 0 R >> endobj".encode())
        # Contents Object
        objects.append(f"{contents_id} 0 obj << /Length {len(stream_content)} >> stream\n".encode() + stream_content + b"\nendstream\nendobj")

    # Fonts
    objects.append(f"{font_regular_id} 0 obj << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> endobj".encode())
    objects.append(f"{font_bold_id} 0 obj << /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >> endobj".encode())
    objects.append(f"{font_courier_id} 0 obj << /Type /Font /Subtype /Type1 /BaseFont /Courier >> endobj".encode())

    # Assemble PDF with cross-reference table
    out = [b"%PDF-1.4\n"]
    offsets = []
    for obj in objects:
        offsets.append(sum(len(x) for x in out))
        out.append(obj + b"\n")

    xref_offset = sum(len(x) for x in out)
    total_objs = len(objects) + 1
    out.append(f"xref\n0 {total_objs}\n0000000000 65535 f \n".encode())
    for off in offsets:
        out.append(f"{off:010d} 00000 n \n".encode())
    out.append(f"trailer << /Size {total_objs} /Root 1 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n".encode())

    with open(output_filename, "wb") as f:
        f.write(b"".join(out))
    print(f"Successfully generated {output_filename}")

if __name__ == "__main__":
    create_chat_history_pdf()
