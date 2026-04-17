# Task 1
import traceback
try:
    with open('diary.txt', 'a') as file:
            # To show the first question only once
            first_prompt =True
            while True:
                if first_prompt:
                    user_input = input('What happened today?').strip().lower()
                    first_prompt = False
                else:
                    user_input = input("What else?").strip().lower()
                if user_input == "done for now":
                    file.write(f'{user_input} \n')
                    break
                file.write(f'{user_input} \n')                            
except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"Exception type: {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")


