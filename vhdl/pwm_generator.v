module pwm_generator (
    input clk,
    input [7:0] duty, // 0-255 duty cycle
    output reg pwm_out
);
    reg [7:0] counter = 0;

    always @(posedge clk) begin
        if (counter < duty)
            pwm_out <= 1;
        else
            pwm_out <= 0;

        counter <= counter + 1;
    end
endmodule
