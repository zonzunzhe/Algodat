import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_callout(cell, border_color_hex="1E3A5F", bg_color_hex="F6F8FA"):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg_color_hex}"/>')
    tcPr.append(shd)
    
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="none"/>\n'
        f'  <w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color_hex}"/>\n'
        f'  <w:bottom w:val="none"/>\n'
        f'  <w:right w:val="none"/>\n'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>\n'
        f'  <w:top w:w="140" w:type="dxa"/>\n'
        f'  <w:left w:w="220" w:type="dxa"/>\n'
        f'  <w:bottom w:w="140" w:type="dxa"/>\n'
        f'  <w:right w:w="200" w:type="dxa"/>\n'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_code_cell(cell):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F8F9FA"/>')
    tcPr.append(shd)
    
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>\n'
        f'  <w:left w:val="single" w:sz="16" w:space="0" w:color="4A5568"/>\n'
        f'  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>\n'
        f'  <w:right w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>\n'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>\n'
        f'  <w:top w:w="120" w:type="dxa"/>\n'
        f'  <w:left w:w="180" w:type="dxa"/>\n'
        f'  <w:bottom w:w="120" w:type="dxa"/>\n'
        f'  <w:right w:w="180" w:type="dxa"/>\n'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_table_styling(table):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="single" w:sz="8" w:space="0" w:color="1E3A5F"/>\n'
        f'  <w:left w:val="none"/>\n'
        f'  <w:bottom w:val="single" w:sz="8" w:space="0" w:color="1E3A5F"/>\n'
        f'  <w:right w:val="none"/>\n'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="E1E4E8"/>\n'
        f'  <w:insideV w:val="none"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def build_document():
    doc = Document()

    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    doc.core_properties.title = "Array-Based Stack Implementation in Java"
    doc.core_properties.author = "Department of Computer Science"
    doc.core_properties.subject = "Algorithms and Data Structures"
    doc.core_properties.category = "Technical Reference"

    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(10.5)
    normal_style.font.color.rgb = RGBColor(0x22, 0x22, 0x22)

    def add_title(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2)
        run = p.add_run(text)
        run.font.name = 'Segoe UI'
        run.font.size = Pt(20)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x1E, 0x3A, 0x5F)
        return p

    def add_meta_line(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(18)
        run = p.add_run(text)
        run.font.name = 'Calibri'
        run.font.size = Pt(9.5)
        run.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
        return p

    def add_heading_1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = 'Segoe UI Semibold'
        run.font.size = Pt(13.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x1E, 0x3A, 0x5F)
        return p

    def add_heading_2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(11)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = 'Segoe UI Semibold'
        run.font.size = Pt(11.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x2E, 0x5B, 0x88)
        return p

    def add_heading_3(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = 'Segoe UI Semibold'
        run.font.size = Pt(10.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
        return p

    def add_p(text, bold_prefix=None, space_after=5):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.font.bold = True
            r_pre.font.color.rgb = RGBColor(0x1E, 0x3A, 0x5F)
        p.add_run(text)
        return p

    def add_callout(label, text, is_warning=False):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        tbl.columns[0].width = Inches(6.5)

        cell = tbl.cell(0, 0)
        border_col = "A03838" if is_warning else "2E5B88"
        bg_col = "FDF8F8" if is_warning else "F4F6F9"
        set_cell_callout(cell, border_color_hex=border_col, bg_color_hex=bg_col)

        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.15

        r_lbl = p.add_run(label + " ")
        r_lbl.font.name = 'Segoe UI Semibold'
        r_lbl.font.bold = True
        r_lbl.font.size = Pt(9.5)
        r_lbl.font.color.rgb = RGBColor(0xA0, 0x38, 0x38) if is_warning else RGBColor(0x1E, 0x3A, 0x5F)

        r_txt = p.add_run(text)
        r_txt.font.name = 'Calibri'
        r_txt.font.size = Pt(9.5)
        r_txt.font.color.rgb = RGBColor(0x22, 0x22, 0x22)

        p_spacer = doc.add_paragraph()
        p_spacer.paragraph_format.space_before = Pt(0)
        p_spacer.paragraph_format.space_after = Pt(3)

    def add_code_block(code_text):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        tbl.columns[0].width = Inches(6.5)

        cell = tbl.cell(0, 0)
        set_code_cell(cell)

        lines = code_text.strip().split("\n")
        first = True
        for line in lines:
            if first:
                p = cell.paragraphs[0]
                first = False
            else:
                p = cell.add_paragraph()
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(1)
            p.paragraph_format.line_spacing = 1.05
            
            run = p.add_run(line)
            run.font.name = 'Consolas'
            run.font.size = Pt(9.0)
            run.font.color.rgb = RGBColor(0x22, 0x22, 0x22)

        p_spacer = doc.add_paragraph()
        p_spacer.paragraph_format.space_before = Pt(0)
        p_spacer.paragraph_format.space_after = Pt(3)

    add_title("Data Structure Specification: Array-Based Stack in Java")
    add_meta_line("Module: Algorithms and Data Structures (Algodat)  |  Target: Undergraduate CS / Junior Developers  |  Language: Java")

    add_heading_1("1. Overview and Abstract Data Type Definition")
    add_p(
        "A stack is a linear collection governed by the Last-In, First-Out (LIFO) protocol. "
        "All element insertions and removals occur at a single end, conventionally designated as top. "
        "The most recently added element is always the first one eligible for removal."
    )

    add_heading_2("1.1 Operational Analogies")
    add_p("Three concrete scenarios illustrate the mechanics of LIFO operations:")

    p1 = doc.add_paragraph(style='List Bullet')
    p1.paragraph_format.space_after = Pt(2)
    p1.add_run("Plate Dispenser: ").bold = True
    p1.add_run("Each tray placed onto the spring-loaded carriage sits above previously loaded trays. Customers take only the top tray; lower trays remain inaccessible until upper trays are cleared.")

    p2 = doc.add_paragraph(style='List Bullet')
    p2.paragraph_format.space_after = Pt(2)
    p2.add_run("Browser History Stack: ").bold = True
    p2.add_run("Visiting URLs pushes addresses sequentially onto the navigation stack. The Back action pops the current address to reveal the immediately preceding page.")

    p3 = doc.add_paragraph(style='List Bullet')
    p3.paragraph_format.space_after = Pt(4)
    p3.add_run("Call Stack Execution: ").bold = True
    p3.add_run("When method A calls method B, the JVM pushes a stack frame for B on top of A. When B finishes execution, its frame pops off, returning execution context to A.")

    add_heading_1("2. Memory Layout and Internal Mechanics")
    add_p(
        "In this concrete implementation, the stack is backed by a fixed-capacity integer array (arr) "
        "and an integer pointer (top). The array occupies contiguous physical memory allocated during object construction."
    )

    var_table = doc.add_table(rows=4, cols=3)
    var_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_styling(var_table)

    col_widths = [Inches(1.4), Inches(1.3), Inches(3.8)]
    headers = ["Field", "Type", "Description and Invariant"]

    for idx, heading in enumerate(headers):
        cell = var_table.rows[0].cells[idx]
        cell.width = col_widths[idx]
        set_cell_background(cell, "1E3A5F")
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(heading)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        r.font.size = Pt(9.5)

    rows = [
        ("arr", "int[]", "Underlying array of fixed length capacity storing elements."),
        ("capacity", "int", "Maximum capacity specified during construction; limits array bounds."),
        ("top", "int", "Index of the current top element. Invariant: -1 <= top < capacity.")
    ]

    for row_idx, data in enumerate(rows, start=1):
        row = var_table.rows[row_idx]
        bg = "FFFFFF" if row_idx % 2 != 0 else "F8FAFC"
        for col_idx, text in enumerate(data):
            cell = row.cells[col_idx]
            cell.width = col_widths[col_idx]
            set_cell_background(cell, bg)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(3)
            r = p.add_run(text)
            r.font.size = Pt(9.0)
            if col_idx == 0:
                r.font.bold = True
                r.font.name = 'Consolas'

    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_before = Pt(0)
    p_spacer.paragraph_format.space_after = Pt(4)

    add_heading_2("2.1 Pointer Initialization (-1 Sentinel)")
    add_p(
        "Java arrays are zero-indexed. An array slot at index 0 represents the first valid element. "
        "Consequently, if top were initialized to 0, it would falsely imply that arr[0] holds a valid entry. "
        "Setting top = -1 establishes a clean sentinel value indicating that no elements have been pushed."
    )

    add_heading_2("2.2 Visual Representation of Pointer Movement")
    add_p(
        "Consider a stack initialized with capacity = 4 after sequential pushes of 10, 20, and 30:"
    )

    diagram = (
        "Memory State:\n"
        "Index:     [ 0 ]   [ 1 ]   [ 2 ]   [ 3 ]\n"
        "Array:    |  10  |  20  |  30  |  --  |\n"
        "                                  ^\n"
        "                                top = 2 (size = 3, capacity = 4)\n\n"
        "After push(40):\n"
        "Array:    |  10  |  20  |  30  |  40  |\n"
        "                                         ^\n"
        "                                       top = 3 (isFull() == true)\n\n"
        "After pop():\n"
        "Array:    |  10  |  20  |  30  | (40) |\n"
        "                                  ^\n"
        "                                top = 2 (value 40 is logically deleted)"
    )
    add_code_block(diagram)

    add_callout(
        "Logical vs Physical Deletion:",
        "Popping an element decrements the top pointer from 3 to 2. The integer 40 remains in memory at arr[3], "
        "but it is logically deleted because all read and write boundaries are dictated solely by top. "
        "A subsequent push operation simply overwrites arr[3]."
    )

    add_heading_2("2.3 Boundary Conditions: Overflow and Underflow")
    add_p(
        "A fixed-size array requires strict boundary enforcement before reading or writing:"
    )

    p_of = doc.add_paragraph(style='List Bullet')
    p_of.paragraph_format.space_after = Pt(2)
    p_of.add_run("Stack Overflow: ").bold = True
    p_of.add_run("Occurs when attempting to push onto a full stack (top == capacity - 1). Writing to arr[top + 1] would exceed array bounds and throw ArrayIndexOutOfBoundsException.")

    p_uf = doc.add_paragraph(style='List Bullet')
    p_uf.paragraph_format.space_after = Pt(4)
    p_uf.add_run("Stack Underflow: ").bold = True
    p_uf.add_run("Occurs when calling pop() or peek() on an empty stack (top == -1). Reading arr[-1] would immediately trigger an out-of-bounds error.")

    add_callout(
        "Off-by-One Warning:",
        "For an array of capacity 4, the highest valid index is 3 (capacity - 1). "
        "Checking 'top == capacity' is an off-by-one bug that allows an illegal write to index 4.",
        is_warning=True
    )

    add_heading_1("3. Implementation Source Code")
    add_p(
        "The following is the complete, self-contained Java class (Stack.java) without external dependencies:"
    )

    source_code = (
        "public class Stack {\n"
        "    int[] arr;\n"
        "    int capacity;\n"
        "    int top;\n\n"
        "    public Stack(int size) {\n"
        "        capacity = size;\n"
        "        arr = new int[capacity];\n"
        "        top = -1;\n"
        "    }\n\n"
        "    public void push(int value) {\n"
        "        if (isFull()) {\n"
        "            System.out.println(\"Stack Overflow! Cannot push \" + value + \" (Stack is full)\");\n"
        "            return;\n"
        "        }\n\n"
        "        top++;\n"
        "        arr[top] = value;\n"
        "        System.out.println(\"Pushed \" + value + \" to stack\");\n"
        "    }\n\n"
        "    public int pop() {\n"
        "        if (isEmpty()) {\n"
        "            System.out.println(\"Stack Underflow! Cannot pop (Stack is empty)\");\n"
        "            return -1;\n"
        "        }\n\n"
        "        int value = arr[top];\n"
        "        top--;\n"
        "        System.out.println(\"Popped \" + value + \" from stack\");\n"
        "        return value;\n"
        "    }\n\n"
        "    public int peek() {\n"
        "        if (isEmpty()) {\n"
        "            System.out.println(\"Stack is empty! Nothing to peek\");\n"
        "            return -1;\n"
        "        }\n\n"
        "        return arr[top];\n"
        "    }\n\n"
        "    public boolean isEmpty() {\n"
        "        return top == -1;\n"
        "    }\n\n"
        "    public boolean isFull() {\n"
        "        return top == capacity - 1;\n"
        "    }\n\n"
        "    public int size() {\n"
        "        return top + 1;\n"
        "    }\n\n"
        "    public void printStack() {\n"
        "        if (isEmpty()) {\n"
        "            System.out.println(\"Stack is empty!\");\n"
        "            return;\n"
        "        }\n\n"
        "        System.out.println(\"Current Stack (top to bottom):\");\n"
        "        for (int i = top; i >= 0; i--) {\n"
        "            System.out.println(\"| \" + arr[i] + \" |\");\n"
        "        }\n"
        "        System.out.println(\"-------\");\n"
        "    }\n"
        "}"
    )
    add_code_block(source_code)

    add_heading_2("3.1 Method Analysis")

    add_heading_3("Constructor: Stack(int size)")
    add_p(
        "Initializes capacity with the specified integer, allocates the contiguous array new int[capacity], "
        "and sets top to -1."
    )

    add_heading_3("push(int value)")
    add_p(
        "1. Invokes isFull() to verify slot availability.\n"
        "2. If full, prints an overflow diagnostic and returns early without mutating state.\n"
        "3. Increments top by 1, advancing the index pointer to the next free cell.\n"
        "4. Assigns value into arr[top]."
    )

    add_heading_3("pop()")
    add_p(
        "1. Invokes isEmpty() to verify whether elements exist.\n"
        "2. If empty, prints an underflow diagnostic and returns sentinel fallback -1.\n"
        "3. Captures arr[top] into a local variable.\n"
        "4. Decrements top by 1, logically dropping the top element.\n"
        "5. Returns the stored value."
    )

    add_heading_3("peek()")
    add_p(
        "Reads arr[top] directly after verifying isEmpty(). Does not decrement top; stack size remains unchanged."
    )

    add_heading_3("Query Methods: isEmpty(), isFull(), size()")
    add_p(
        "• isEmpty(): Evaluates top == -1 (boolean).\n"
        "• isFull(): Evaluates top == capacity - 1 (boolean).\n"
        "• size(): Returns top + 1, translating the zero-based index to an 1-based cardinal count."
    )

    add_heading_3("printStack()")
    add_p(
        "Iterates from top downward to index 0, outputting elements in vertical LIFO order."
    )

    add_heading_1("4. Complexity Analysis")
    add_p(
        "Because array index calculations translate directly to constant base-address offsets in hardware, "
        "all core operations execute in O(1) time without element shifting."
    )

    comp_table = doc.add_table(rows=6, cols=3)
    comp_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_styling(comp_table)

    comp_widths = [Inches(1.5), Inches(1.5), Inches(3.5)]
    comp_headers = ["Operation", "Time Complexity", "Mechanics"]

    for idx, heading in enumerate(comp_headers):
        cell = comp_table.rows[0].cells[idx]
        cell.width = comp_widths[idx]
        set_cell_background(cell, "1E3A5F")
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(heading)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        r.font.size = Pt(9.5)

    cdata = [
        ("push(v)", "O(1)", "Single index calculation and array write: arr[++top] = v."),
        ("pop()", "O(1)", "Single index read and pointer decrement: arr[top--]."),
        ("peek()", "O(1)", "Direct memory lookup at arr[top]; no pointer modification."),
        ("isEmpty()", "O(1)", "Single integer equality comparison (top == -1)."),
        ("printStack()", "O(n)", "Linear iteration over all n active elements from top to 0.")
    ]

    for row_idx, data in enumerate(cdata, start=1):
        row = comp_table.rows[row_idx]
        bg = "FFFFFF" if row_idx % 2 != 0 else "F8FAFC"
        for col_idx, text in enumerate(data):
            cell = row.cells[col_idx]
            cell.width = comp_widths[col_idx]
            set_cell_background(cell, bg)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(3)
            r = p.add_run(text)
            r.font.size = Pt(9.0)
            if col_idx == 0:
                r.font.bold = True
                r.font.name = 'Consolas'
            elif col_idx == 1:
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x5F)

    p_spacer2 = doc.add_paragraph()
    p_spacer2.paragraph_format.space_before = Pt(0)
    p_spacer2.paragraph_format.space_after = Pt(4)

    add_heading_2("4.1 Space Complexity")
    add_p(
        "• Space: O(n), where n = capacity.\n"
        "Memory for the array is allocated upfront upon instantiation. "
        "The footprint is continuous in RAM, offering excellent CPU cache locality."
    )

    add_heading_1("5. Demonstration Test Suite and Console Output")
    add_p(
        "The main() method exercises nominal push/pop cycles along with explicit boundary tests (overflow and underflow):"
    )

    main_code = (
        "public static void main(String[] args) {\n"
        "    System.out.println(\"--- Stack Demo for Beginners ---\\n\");\n\n"
        "    Stack stack = new Stack(4);\n"
        "    System.out.println(\"Created stack with capacity 4.\");\n"
        "    System.out.println(\"Is stack empty? \" + stack.isEmpty());\n\n"
        "    System.out.println(\"\\n--- Pushing elements ---\");\n"
        "    stack.push(10);\n"
        "    stack.push(20);\n"
        "    stack.push(30);\n\n"
        "    System.out.println(\"\\n--- Printing Stack ---\");\n"
        "    stack.printStack();\n\n"
        "    System.out.println(\"\\n--- Peeking ---\");\n"
        "    System.out.println(\"Top element is: \" + stack.peek());\n"
        "    System.out.println(\"Stack size is: \" + stack.size());\n\n"
        "    System.out.println(\"\\n--- Testing Overflow ---\");\n"
        "    stack.push(40);\n"
        "    System.out.println(\"Is stack full? \" + stack.isFull());\n"
        "    stack.push(50);\n\n"
        "    System.out.println(\"\\n--- Popping elements ---\");\n"
        "    stack.pop();\n"
        "    stack.pop();\n"
        "    stack.printStack();\n\n"
        "    System.out.println(\"\\n--- Testing Underflow ---\");\n"
        "    stack.pop();\n"
        "    stack.pop();\n"
        "    System.out.println(\"Is stack empty? \" + stack.isEmpty());\n"
        "    stack.pop();\n"
        "}"
    )
    add_code_block(main_code)

    add_heading_2("5.1 Verifiable Console Output")
    add_p("Compiling and executing Stack.java yields:")

    console_output = (
        "--- Stack Demo for Beginners ---\n\n"
        "Created stack with capacity 4.\n"
        "Is stack empty? true\n\n"
        "--- Pushing elements ---\n"
        "Pushed 10 to stack\n"
        "Pushed 20 to stack\n"
        "Pushed 30 to stack\n\n"
        "--- Printing Stack ---\n"
        "Current Stack (top to bottom):\n"
        "| 30 |\n"
        "| 20 |\n"
        "| 10 |\n"
        "-------\n\n"
        "--- Peeking ---\n"
        "Top element is: 30\n"
        "Stack size is: 3\n\n"
        "--- Testing Overflow ---\n"
        "Pushed 40 to stack\n"
        "Is stack full? true\n"
        "Stack Overflow! Cannot push 50 (Stack is full)\n\n"
        "--- Popping elements ---\n"
        "Popped 40 from stack\n"
        "Popped 30 from stack\n"
        "Current Stack (top to bottom):\n"
        "| 20 |\n"
        "| 10 |\n"
        "-------\n\n"
        "--- Testing Underflow ---\n"
        "Popped 20 from stack\n"
        "Popped 10 from stack\n"
        "Is stack empty? true\n"
        "Stack Underflow! Cannot pop (Stack is empty)"
    )
    add_code_block(console_output)

    add_heading_1("6. Engineering Notes: Array Stack vs. java.util.Stack")
    add_p(
        "In Java's standard library, java.util.Stack is historically provided, but modern codebases avoid it for two specific architectural reasons:"
    )

    p_dep1 = doc.add_paragraph(style='List Bullet')
    p_dep1.paragraph_format.space_after = Pt(2)
    p_dep1.add_run("Inheritance Violation: ").bold = True
    p_dep1.add_run("java.util.Stack extends java.util.Vector. Because Vector is a list, methods like add(index, element) are exposed, allowing callers to insert into arbitrary positions and violating strict LIFO semantics.")

    p_dep2 = doc.add_paragraph(style='List Bullet')
    p_dep2.paragraph_format.space_after = Pt(4)
    p_dep2.add_run("Synchronization Overhead: ").bold = True
    p_dep2.add_run("Vector methods are synchronized on every call, incurring thread-locking performance overhead in single-threaded contexts. Java official documentation recommends java.util.ArrayDeque when a library stack is needed.")

    add_p(
        "Building a raw array-based stack as implemented above provides clear insight into how index pointer arithmetic, memory bounds, and LIFO discipline function without hidden library overhead."
    )

    output_filename = "Java_Stack_Junior_Guide.docx"
    doc.save(output_filename)
    print(f"Generated clean technical document: '{output_filename}' ({os.path.getsize(output_filename):,} bytes).")

if __name__ == "__main__":
    build_document()
