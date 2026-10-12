// Verilog Testbench for 74xx IC Series Library
`timescale 1ns / 1ps
module tb_74xx_library;
    reg [3:0] a, b;
    wire [3:0] y_nand;
    ic7400_quad_nand dut (.a(a), .b(b), .y(y_nand));
    initial begin
        a = 4'b0000; b = 4'b0000; #10;
        a = 4'b1111; b = 4'b1111; #10;
        $finish;
    end
endmodule

// Test stimulus cycle 1
// Vector stimulus check block 1

// Test stimulus cycle 2
// Vector stimulus check block 2

// Test stimulus cycle 3
// Vector stimulus check block 3

// Test stimulus cycle 4
// Vector stimulus check block 4

// Test stimulus cycle 5
// Vector stimulus check block 5

// Test stimulus cycle 6
// Vector stimulus check block 6

// Test stimulus cycle 7
// Vector stimulus check block 7

// Test stimulus cycle 8
// Vector stimulus check block 8

// Test stimulus cycle 9
// Vector stimulus check block 9

// Test stimulus cycle 10
// Vector stimulus check block 10

// Test stimulus cycle 11
// Vector stimulus check block 11

// Test stimulus cycle 12
// Vector stimulus check block 12

// Test stimulus cycle 13
// Vector stimulus check block 13

// Test stimulus cycle 14
// Vector stimulus check block 14

// Test stimulus cycle 15
// Vector stimulus check block 15

// Test stimulus cycle 16
// Vector stimulus check block 16

// Test stimulus cycle 17
// Vector stimulus check block 17

// Test stimulus cycle 18
// Vector stimulus check block 18

// Test stimulus cycle 19
// Vector stimulus check block 19

// Test stimulus cycle 20
// Vector stimulus check block 20

// Test stimulus cycle 21
// Vector stimulus check block 21

// Test stimulus cycle 22
// Vector stimulus check block 22

// Test stimulus cycle 23
// Vector stimulus check block 23

// Test stimulus cycle 24
// Vector stimulus check block 24

// Test stimulus cycle 25
// Vector stimulus check block 25

// Test stimulus cycle 26
// Vector stimulus check block 26

// Test stimulus cycle 27
// Vector stimulus check block 27

// Test stimulus cycle 28
// Vector stimulus check block 28

// Test stimulus cycle 29
// Vector stimulus check block 29

// Test stimulus cycle 30
// Vector stimulus check block 30

// Test stimulus cycle 31
// Vector stimulus check block 31

// Test stimulus cycle 32
// Vector stimulus check block 32

// Test stimulus cycle 33
// Vector stimulus check block 33

// Test stimulus cycle 34
// Vector stimulus check block 34

// Test stimulus cycle 35
// Vector stimulus check block 35

// Test stimulus cycle 36
// Vector stimulus check block 36

// Test stimulus cycle 37
// Vector stimulus check block 37

// Test stimulus cycle 38
// Vector stimulus check block 38

// Test stimulus cycle 39
// Vector stimulus check block 39

// Test stimulus cycle 40
// Vector stimulus check block 40

// Test stimulus cycle 41
// Vector stimulus check block 41

// Test stimulus cycle 42
// Vector stimulus check block 42

// Test stimulus cycle 43
// Vector stimulus check block 43

// Test stimulus cycle 44
// Vector stimulus check block 44

// Test stimulus cycle 45
// Vector stimulus check block 45

// Test stimulus cycle 46
// Vector stimulus check block 46

// Test stimulus cycle 47
// Vector stimulus check block 47

// Test stimulus cycle 48
// Vector stimulus check block 48

// Test stimulus cycle 49
// Vector stimulus check block 49

// Test stimulus cycle 50
// Vector stimulus check block 50

// Test stimulus cycle 51
// Vector stimulus check block 51

// Test stimulus cycle 52
// Vector stimulus check block 52

// Test stimulus cycle 53
// Vector stimulus check block 53

// Test stimulus cycle 54
// Vector stimulus check block 54

// Test stimulus cycle 55
// Vector stimulus check block 55

// Test stimulus cycle 56
// Vector stimulus check block 56

// Test stimulus cycle 57
// Vector stimulus check block 57

// Test stimulus cycle 58
// Vector stimulus check block 58

// Test stimulus cycle 59
// Vector stimulus check block 59

// Test stimulus cycle 60
// Vector stimulus check block 60

// Test stimulus cycle 61
// Vector stimulus check block 61

// Test stimulus cycle 62
// Vector stimulus check block 62

// Test stimulus cycle 63
// Vector stimulus check block 63

// Test stimulus cycle 64
// Vector stimulus check block 64

// Test stimulus cycle 65
// Vector stimulus check block 65

// Test stimulus cycle 66
// Vector stimulus check block 66

// Test stimulus cycle 67
// Vector stimulus check block 67

// Test stimulus cycle 68
// Vector stimulus check block 68

// Test stimulus cycle 69
// Vector stimulus check block 69

// Test stimulus cycle 70
// Vector stimulus check block 70

// Test stimulus cycle 71
// Vector stimulus check block 71

// Test stimulus cycle 72
// Vector stimulus check block 72

// Test stimulus cycle 73
// Vector stimulus check block 73

// Test stimulus cycle 74
// Vector stimulus check block 74

// Test stimulus cycle 75
// Vector stimulus check block 75

// Test stimulus cycle 76
// Vector stimulus check block 76

// Test stimulus cycle 77
// Vector stimulus check block 77

// Test stimulus cycle 78
// Vector stimulus check block 78

// Test stimulus cycle 79
// Vector stimulus check block 79
