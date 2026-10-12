// Synthesizable Verilog HDL Modules: Combinational Logic
module and_gate_2input (input wire a, input wire b, output wire y);
    assign y = a & b;
endmodule

module nand_gate_2input (input wire a, input wire b, output wire y);
    assign y = ~(a & b);
endmodule

module half_adder (input wire a, input wire b, output wire sum, output wire carry);
    assign sum = a ^ b;
    assign carry = a & b;
endmodule

module full_adder (input wire a, input wire b, input wire cin, output wire sum, output wire cout);
    assign sum = a ^ b ^ cin;
    assign cout = (a & b) | (b & cin) | (a & cin);
endmodule

module logic_slice_stage_1 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_2 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_3 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_4 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_5 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_6 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_7 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_8 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_9 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_10 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_11 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_12 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_13 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_14 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_15 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_16 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_17 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_18 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_19 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_20 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_21 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_22 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_23 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_24 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_25 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_26 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_27 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_28 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_29 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_30 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_31 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_32 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_33 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_34 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_35 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_36 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_37 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_38 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_39 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_40 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_41 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_42 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_43 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_44 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_45 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_46 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_47 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_48 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_49 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_50 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_51 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_52 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_53 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_54 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_55 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_56 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_57 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_58 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_59 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_60 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_61 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_62 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_63 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_64 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_65 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_66 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_67 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_68 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_69 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_70 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_71 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_72 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_73 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_74 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_75 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_76 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_77 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_78 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_79 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_80 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_81 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_82 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_83 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_84 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_85 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_86 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_87 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_88 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_89 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_90 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_91 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_92 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_93 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_94 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_95 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_96 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_97 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_98 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_99 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_100 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_101 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_102 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_103 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_104 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_105 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_106 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_107 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_108 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_109 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_110 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_111 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_112 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_113 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_114 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_115 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_116 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_117 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_118 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule

module logic_slice_stage_119 (input wire [3:0] in_a, input wire [3:0] in_b, output wire [3:0] out_res);
    assign out_res = in_a ^ in_b;
endmodule
