Model: GPT-4

> Word Macros. Write a Word Macro that will find all Python or SQL code within a Document and assign it to a 'code' Style using a fixed width font type.
> 
> 1 / 1

To create a Word Macro that will find all Python or SQL code within a document and assign it to a 'code' style using a fixed-width font type, follow these steps:

1.  Open Microsoft Word.
2.  Press ALT+F11 to open the Visual Basic for Applications (VBA) editor.
3.  In the VBA editor, go to "Insert" > "Module" to create a new module.
4.  Copy and paste the following VBA code into the new module:

vba

```vba
Option Explicit

Sub FormatCodeBlocks()
    Dim codeStyle As Style
    Dim codeRegExp As Object
    Dim codeMatches As Object
    Dim match As Object
    Dim searchRange As Range
    Dim codeRange As Range
    
    ' Create or update the 'code' style
    On Error Resume Next
    Set codeStyle = ActiveDocument.Styles("code")
    If codeStyle Is Nothing Then
        Set codeStyle = ActiveDocument.Styles.Add(Name:="code", Type:=wdStyleTypeCharacter)
    End If
    On Error GoTo 0
    
    With codeStyle.Font
        .Name = "Courier New"
        .Size = 10
    End With
    
    ' Define a regular expression pattern to identify Python or SQL code blocks
    Set codeRegExp = CreateObject("VBScript.RegExp")
    With codeRegExp
        .Pattern = "(```(python|sql)(?:\r?\n)((?:.|\r?\n)+?)```)"
        .Global = True
        .IgnoreCase = True
        .MultiLine = True
```

1 / 1

> is that code complete? Don't output it again, just continue if it's not, if it's complete say so.
> 
> 2 / 2

Apologies for the incomplete code. Here's the continuation of the code snippet:

vba

    ```vba
End With

    ' Search for code blocks in the document
    Set searchRange = ActiveDocument.Content
    Set codeMatches = codeRegExp.Execute(searchRange.Text)

    ' Apply the 'code' style to the code blocks
    For Each match In codeMatches
        Set codeRange = searchRange.Duplicate
        codeRange.Start = searchRange.Start + match.FirstIndex
        codeRange.End = codeRange.Start + Len(match.Value)
        codeRange.Style = codeStyle
    Next match
End Sub
```

Now the code is complete. You can run the macro by pressing F5 in the VBA editor or by going to the "Developer" tab in Word and clicking "Macros," selecting the "FormatCodeBlocks" macro, and clicking "Run." The macro will find all Python or SQL code blocks in the document and apply the 'code' style using a fixed-width font type.

1 / 1