import tkinter 
from tkinter.filedialog import askopenfilenames 
import customtkinter 
import algorithms 
import pandas as pd 
 
customtkinter.set_appearance_mode("dark"); 
customtkinter.set_default_color_theme("blue"); 
 
app = customtkinter.CTk() 
app.geometry("400x500") 


 

def is_float(value):
  """Check if value is a float"""
  try:
      float(value)
      return True
  except ValueError:
      return False
 
# make a standard button 
def make_button(st,fun,pos): 
  """Make a standard button"""
  button = customtkinter.CTkButton(master=app, 
                                  text=st, 
                                  width=200, 
                                  command=fun); 
  button.place(relx=pos[0],rely=pos[1],anchor=tkinter.CENTER) 
 
# make a back button 
def make_back_button(fun): 
  button = customtkinter.CTkButton(master=app, 
                                  text="Back", 
                                  width=80, 
                                  command=fun); 
  button.place(relx=.25,rely=.85,anchor=tkinter.CENTER) 
 
 
# make astandard frame 
def make_frame(): 
  frame = customtkinter.CTkFrame(master=app, 
                                width=300, 
                                height=400, 
                                corner_radius=10) 
  frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER) 
 
# make a standerd label 
def make_label(st,pos): 
  label = customtkinter.CTkLabel(master=app, 
                                text=st, 
                                width=200, 
                                height=25, 
                                bg_color="#fff0e1", 
                                text_color="#664e04", 
                                font=("Arial", 18) 
                                ) 
  label.place(relx=pos[0], rely=pos[1], anchor=tkinter.CENTER) 
 
 
 
def make_input(pos): 
  entry = customtkinter.CTkEntry(master=app, 
                                width=200, 
                                height=25, 
                                corner_radius=10) 
  entry.place(relx=pos[0], rely=pos[1], anchor=tkinter.CENTER) 
 
def make_option_menu(values, default, callback, pos): 
    global choice 
    combobox = customtkinter.CTkOptionMenu(master=app, 
                                           values=values, 
                                           command=callback) 
    combobox.place(relx=pos[0],rely=pos[1],anchor=tkinter.CENTER) 
    combobox.set(default) 
#---------------------------------------------------------------- 
 
 
def destroy_all():
  """Destroy all widgets""" 
  for w in app.winfo_children(): 
    w.destroy(); 
 
 
def load_dataset():
  """prompt user to select a file and load it into dataset""" 
  csv_file_path = askopenfilenames() 
  algorithms.dataset=pd.read_csv(csv_file_path[0]) 
   
    
   
 
 
#display algoritms windows 
 #n_features = number of features for RFE
def select_algorithm(n_features): 
  """Select algorithm window"""
  if algorithms.dataset is None: 
   tkinter.messagebox.showerror("Dataset Error","UPLOAD DATASET, PLEASE!!") 
   return
 
  if n_features == "": 
    tkinter.messagebox.showerror("Features Error ","ENTER NUMBER OF FEATURES, PLEASE!! ") 
    return
   
  if  n_features.isdigit() == False: 
    tkinter.messagebox.showerror("Features Error ","INVALID NUMBER !! ") 
    return
  
  algorithms.num_feature = int(n_features)
  # algorithms.RFE()
  destroy_all(); 
  make_frame(); 
  make_label("Select Algorithm", [.5,.3]); 
  make_button("SVM",SVM_window, [.5,.4]); 
  make_button("Dession Tree",algorithms.dession_tree, [.5,.5]); 
  make_button("KNN",algorithms.KNN, [.5,.6]); 
  make_back_button(classification); 
   
 
 
#classification window 
 
def classification(): 
  """Classification window"""
  destroy_all(); 
  make_frame(); 
  make_button("Load Dataset", load_dataset, [.5,.3]); 
  make_label("Enter feature number", [.5,.4]) 
 
  entry = customtkinter.CTkEntry(master=app, 
                                 width=200, 
                                height=25, 
                                  corner_radius=10) 
  entry.place(relx=.5, rely=.5, anchor=tkinter.CENTER) 
 
  def get_input(): 
    #the entry.get() here is the number of features
    select_algorithm(entry.get()); 
 
  make_button("Submmit", get_input, [.5,.7]); 
 
  make_back_button(main_window); 
 
 
 
 
 
 
def main_window(): 
  destroy_all();
  make_frame() 
  make_label("machine learning project", [.5,.3]) 
  make_button("Classification", classification, [.5,.5]) 
 
 
def SVM_window():
  destroy_all(); 
  make_frame(); 
  make_label("SVM", [.5,.3]) 
  #function that assigns the selected choice to the global variable kernel 
  def kernelmenu_callback(choice): 
    global kernel
    if choice == "":
      kernel = "rbf"
    else:
      kernel = choice 
  make_option_menu(["linear", "rbf"], "rbf", kernelmenu_callback, [.5,.4]) 
  make_button("Submmit", train_test, [.5,.7]) 
  make_back_button(select_algorithm) 
 
def train_test(): 
  destroy_all(); 
  make_frame(); 
  make_label("Train & Test", [.5,.3]) 
  make_label("Enter test size", [.5,.4]) 
  entry = customtkinter.CTkEntry(master=app, 
                                 width=200, 
                                 height=25, 
                                 corner_radius=10) 
  entry.place(relx=.5, rely=.5, anchor=tkinter.CENTER) 


  def get_input(): 
    if is_float(entry.get()) == False:
      tkinter.messagebox.showerror("Test size Error","INVALID TEST SIZE !! ")
      return
    algorithms.SVM(kernel,float(entry.get()));  #the entry.get() is the test size
    show_result()

  make_button("Submmit", get_input, [.5,.7]) 
  make_back_button(SVM_window)
 

def show_result():
  destroy_all(); 
  make_frame(); 
  make_label("Results", [.5,.18]) 
  make_label("Accuracy", [.5,.27]) 
  make_label(str(algorithms.accuracy), [.5,.32]) 
  make_label("Precision", [.5,.42]) 
  make_label(str(algorithms.precision), [.5,.47]) 
  make_label("Recall", [.5,.57]) 
  make_label(algorithms.recall, [.5,.62]) 
  make_label("F1 Score", [.5,.72])
  make_label(algorithms.f1_score, [.5,.77])
  make_back_button(main_window)
    
main_window(); 


 
app.mainloop()