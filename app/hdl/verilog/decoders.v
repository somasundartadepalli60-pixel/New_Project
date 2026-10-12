// Synthesizable Verilog HDL Decoders
module decoder_3to8 (input wire [2:0] sel, input wire en, output reg [7:0] out_n);
    always @(*) begin
        if (!en)
            out_n = 8'hFF;
        else
            out_n = ~(8'b1 << sel);
    end
endmodule

module decoder_slice_1 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_2 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_3 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_4 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_5 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_6 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_7 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_8 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_9 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_10 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_11 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_12 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_13 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_14 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_15 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_16 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_17 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_18 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_19 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_20 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_21 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_22 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_23 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_24 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_25 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_26 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_27 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_28 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_29 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_30 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_31 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_32 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_33 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_34 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_35 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_36 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_37 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_38 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_39 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_40 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_41 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_42 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_43 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_44 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_45 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_46 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_47 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_48 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_49 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_50 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_51 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_52 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_53 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_54 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_55 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_56 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_57 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_58 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_59 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_60 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_61 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_62 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_63 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_64 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_65 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_66 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_67 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_68 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_69 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_70 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_71 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_72 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_73 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_74 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_75 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_76 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_77 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_78 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_79 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_80 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_81 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_82 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_83 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_84 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_85 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_86 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_87 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_88 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_89 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_90 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_91 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_92 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_93 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_94 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_95 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_96 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_97 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_98 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule

module decoder_slice_99 (input wire [1:0] in_bits, output reg [3:0] out_active);
    always @(*) begin
        out_active = 4'b0001 << in_bits;
    end
endmodule
