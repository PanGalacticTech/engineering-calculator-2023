Attribute VB_Name = "unitCalc"
Function unitCalc(VALUE As Double, NAME As String)
Dim Tera As String
Tera = "T"
Giga = "G"
Mega = "M"
Kilo = "k"
centi = "c"
milli = "m"
nano = "n"
micro = "u"
pico = "p"
femto = "f"

Dim firstChar As String
firstChar = Left(NAME, 1)

    Select Case firstChar
        Case Tera
            OUTPUT = (VALUE * (10 ^ 12))
        Case Giga
            OUTPUT = (VALUE * (10 ^ 9))
        Case Mega
            OUTPUT = (VALUE * (10 ^ 6))
        Case Kilo
            OUTPUT = (VALUE * (10 ^ 3))
        Case centi
            OUTPUT = (VALUE * (10 ^ -2))
        Case milli
            OUTPUT = (VALUE * (10 ^ -3))
        Case micro
            OUTPUT = (VALUE * (10 ^ -6))
        Case nano
            OUTPUT = (VALUE * (10 ^ -9))
        Case pico
            OUTPUT = (VALUE * (10 ^ -12))
        Case femto
            OUTPUT = (VALUE * (10 ^ -15))
        Case Else
            OUTPUT = VALUE
        End Select
    unitCalc = OUTPUT
End Function

Function UnitGet(VALUE As Double, UNITBASE As String)
Dim OUTPUT As String
    If VALUE < 0 Then
        VALUE = VALUE * -1
    End If
    
    Select Case VALUE
        Case 10 ^ 12 To 10 ^ 15
            OUTPUT = "T"
        Case 10 ^ 9 To 10 ^ 12
            OUTPUT = "G"
        Case 10 ^ 6 To (10 ^ 9)
            OUTPUT = "M"
        Case 10 ^ 3 To (10 ^ 6)
            OUTPUT = "k"
            
        Case 1 To (10 ^ 3)
            OUTPUT = ""
            
        Case (10 ^ -3) To 1
            OUTPUT = "m"
        Case (10 ^ -6) To (10 ^ -3)
            OUTPUT = "u"
        Case (10 ^ -9) To (10 ^ -6)
            OUTPUT = "n"
        Case 10 ^ -12 To (10 ^ -9)
            OUTPUT = "p"
        Case 0 To (10 ^ -12)
            OUTPUT = "f"
        End Select
                
    UnitGet = OUTPUT + UNITBASE
End Function


Function UnitDiv(VALUE As Double, NAME As String)
Tera = "T"
Giga = "G"
Mega = "M"
Kilo = "k"
centi = "c"
milli = "m"
nano = "n"
micro = "u"
pico = "p"
femto = "f"

Dim firstChar As String
firstChar = Left(NAME, 1)

Select Case firstChar
        Case Tera
            OUTPUT = (VALUE / (10 ^ 12))
        Case Giga
            OUTPUT = (VALUE / (10 ^ 9))
        Case Mega
            OUTPUT = (VALUE / (10 ^ 6))
        Case Kilo
            OUTPUT = (VALUE / (10 ^ 3))
        Case centi
            OUTPUT = (VALUE / (10 ^ -2))
        Case milli
            OUTPUT = (VALUE / (10 ^ -3))
        Case micro
            OUTPUT = (VALUE / (10 ^ -6))
        Case nano
            OUTPUT = (VALUE / (10 ^ -9))
        Case pico
            OUTPUT = (VALUE / (10 ^ -12))
        Case femto
            OUTPUT = (VALUE / (10 ^ -15))
        Case Else
            OUTPUT = VALUE
        End Select
    UnitDiv = OUTPUT


End Function

Function pcDiff(VALUE_A As Double, VALUE_B As Double)
Dim difference As Double
Dim ave As Double

    difference = VALUE_A - VALUE_B
    ave = (VALUE_A + VALUE_B) / 2
    pcDiff = (difference / ave) * 100

End Function


