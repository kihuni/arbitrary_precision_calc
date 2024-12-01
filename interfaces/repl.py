class CalculatorREPL:
    def __init__(self, calculator):
        self.calculator = calculator
    
    def run(self):
        """
        Interactive Read-Eval-Print Loop
        
        Features:
        - Multi-base support
        - Scientific functions
        - Error handling
        """
        print("Enhanced Arbitrary Precision Calculator")
        print("Supported features:")
        print("- Multi-base calculations")
        print("- Scientific operations")
        print("Enter calculations. Type 'exit' to quit.")
        
        while True:
            try:
                user_input = input(">>> ")
                
                if user_input.lower() in ['exit', 'quit', 'q']:
                    break
                
                result = self.calculator.evaluate(user_input)
                print(result)
            
            except Exception as e:
                print(f"Error: {e}")