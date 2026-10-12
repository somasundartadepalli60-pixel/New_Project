// Synthesizable Verilog HDL Counters
module sync_counter_4bit (input wire clk, input wire rst_n, input wire en, output reg [3:0] count);
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            count <= 4'b0000;
        else if (en)
            count <= count + 1'b1;
    end
endmodule

module decade_counter_node_1 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_2 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_3 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_4 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_5 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_6 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_7 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_8 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_9 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_10 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_11 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_12 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_13 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_14 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_15 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_16 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_17 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_18 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_19 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_20 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_21 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_22 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_23 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_24 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_25 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_26 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_27 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_28 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_29 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_30 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_31 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_32 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_33 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_34 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_35 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_36 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_37 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_38 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_39 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_40 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_41 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_42 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_43 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_44 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_45 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_46 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_47 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_48 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_49 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_50 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_51 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_52 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_53 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_54 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_55 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_56 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_57 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_58 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_59 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_60 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_61 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_62 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_63 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_64 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_65 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_66 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_67 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_68 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_69 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_70 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_71 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_72 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_73 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_74 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_75 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_76 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_77 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_78 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_79 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_80 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_81 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_82 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_83 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_84 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_85 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_86 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_87 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_88 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule

module decade_counter_node_89 (input wire clk, input wire rst, output reg [3:0] bcd);
    always @(posedge clk) begin
        if (rst || bcd == 4'd9)
            bcd <= 4'd0;
        else
            bcd <= bcd + 1'b1;
    end
endmodule
