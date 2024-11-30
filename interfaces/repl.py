class CalculatorREPL:
    def __init__(self, calculator):
        self.calculator = calculator
    
    def run(self):
        """
        Interactive Read-Eval-Print Loop
        
        Features:
        - Continuous input
        - Error handling
        - Exit commands
        """
        print("Arbitrary Precision Calculator")
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