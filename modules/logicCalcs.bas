Attribute VB_Name = "Module4"
Function doAND(A As Integer, B As Integer)
Dim OUTPUT As Integer
OUTPUT = 0
    If A > 0 And B > 0 Then
        OUTPUT = 1
    Else
        OUTPUT = 0
    End If
doAND = OUTPUT
End Function

Function doOR(A As Integer, B As Integer)
Dim OUTPUT As Integer
OUTPUT = 0
    If A > 0 Or B > 0 Then
        OUTPUT = 1
    Else
        OUTPUT = 0
    End If
doOR = OUTPUT
End Function

Function doNAND(A As Integer, B As Integer)
Dim OUTPUT As Integer
OUTPUT = 0
    If A > 0 And B > 0 Then
        OUTPUT = 0
    Else
        OUTPUT = 1
    End If
doNAND = OUTPUT
End Function

Function doNAND3(A As Integer, B As Integer, C As Integer)
Dim OUTPUT As Integer
OUTPUT = 0
    If A = 0 And B = 0 And C = 0 Then
        OUTPUT = 1
    Else
        OUTPUT = 0
    End If
doNAND3 = OUTPUT
End Function

Function doNOR(A As Integer, B As Integer)
Dim OUTPUT As Integer
OUTPUT = 0
    If A > 0 Or B > 0 Then
        OUTPUT = 0
    Else
        OUTPUT = 1
    End If
doNOR = OUTPUT
End Function

Function doXOR(A As Integer, B As Integer)
Dim OUTPUT As Integer
OUTPUT = 0
    If A > 0 And B = 0 Or A = 0 And B > 0 Then
        OUTPUT = 1
    Else
        OUTPUT = 0
    End If
doXOR = OUTPUT
End Function
Function doXOR3(A As Integer, B As Integer, C As Integer)
Dim OUTPUT As Integer
OUTPUT = 0
    If A + B + C = 1 Then
        OUTPUT = 1
    Else
        OUTPUT = 0
    End If
doXOR3 = OUTPUT
End Function

Function doXNOR(A As Integer, B As Integer)
Dim OUTPUT As Integer
OUTPUT = 0
    If A > 0 And B = 0 Or A = 0 And B > 0 Then
        OUTPUT = 0
    Else
        OUTPUT = 1
    End If
doXNOR = OUTPUT
End Function


Function doNOT(A As Integer)
Dim OUTPUT As Integer
OUTPUT = 0
   If A > 0 Then
        OUTPUT = 0
    Else
        OUTPUT = 1
    End If
doNOT = OUTPUT
End Function

Sub flipS()

If Range("SET").VALUE = 0 Then
    Range("SET").VALUE = "1"
    ElseIf Range("SET").VALUE = 1 Then
    Range("SET").VALUE = "0"
End If

End Sub

Sub flipR()

If Range("RESET").VALUE = 0 Then
    Range("RESET").VALUE = "1"
    ElseIf Range("RESET").VALUE = 1 Then
    Range("RESET").VALUE = "0"
End If

End Sub


