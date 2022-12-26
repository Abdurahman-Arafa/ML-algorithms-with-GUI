import tkinter 
from tkinter.filedialog import askopenfilename
import customtkinter 
import algorithms 
import pandas as pd 
 
customtkinter.set_appearance_mode("dark"); 
customtkinter.set_default_color_theme("blue"); 
 
app = customtkinter.CTk() 
app.geometry("400x500") 
app.title("Machine Learning App")
icon = tkinter.PhotoImage(file = r"C:\Users\abdob\OneDrive\Desktop\el nahas proj\proj\data-mining-project\icon\icon.png")
app.iconphoto(False, icon)

#---------------------------------------------------------------

 
# make a standard button 
def make_button(st,fun,pos, width=200): 
  """Make a standard button"""
  button = customtkinter.CTkButton(master=app, 
                                  text=st, 
                                  width=width, 
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
def make_label(st,pos,size=18): 
  label = customtkinter.CTkLabel(master=app, 
                                text=st, 
                                width=200, 
                                height=25, 
                                bg_color="#ffdf76", 
                                text_color="#664e04", 
                                font=("Arial", size) 
                                ) 
  label.place(relx=pos[0], rely=pos[1], anchor=tkinter.CENTER) 
 
 
 
def make_input(pos): 
  entry = customtkinter.CTkEntry(master=app, 
                                width=200, 
                                height=25, 
                                corner_radius=10) 
  entry.place(relx=pos[0], rely=pos[1], anchor=tkinter.CENTER) 
 
def make_option_menu(values, callback, pos): 
    global choice 
    combobox = customtkinter.CTkOptionMenu(master=app, 
                                           values=values, 
                                           width=200,
                                           command=callback) 
    combobox.place(relx=pos[0],rely=pos[1],anchor=tkinter.CENTER) 
    combobox.set('choose kernel')

#---------------------------------------------------------------- 

 
def is_float_in_range(input):
  """Check if the input is a float number between 0 and 1"""
  try:
      value = float(input)
      if value > 0 and value < 1:
          return True
      else:
          return False
  except ValueError:
      return False

def destroy_all():
  """Destroy all widgets""" 
  for w in app.winfo_children(): 
    w.destroy(); 
 
 
def load_dataset():
  """prompt user to select a file and load it into dataset""" 
  csv_file_path = askopenfilename(filetypes=[("CSV files", "*.csv")])
  algorithms.dataset=pd.read_csv(csv_file_path) 
   
 #-------------------------------------------------------------------   
 

def show_result_view(alg):
  """show the result view"""

  if not hasattr(algorithms, 'accuracy'):
    tkinter.messagebox.showerror("Test Error","Please test the data first !! ")
    return
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
  make_back_button(lambda:train_test_window(alg))

  def back_to_main():
    """delete the attributes and go back to main window"""
    algorithms.dataset = None
    del algorithms.model
    del algorithms.conf_matrix
    del algorithms.accuracy
    del algorithms.precision
    del algorithms.recall
    del algorithms.f1_score
    main_window()
  make_button("home", back_to_main, [.75,.85],80)


def train_test_window(alg): #s-->svm || t--> dession tree || k-->knn 
  destroy_all(); 
  make_frame(); 
  make_label("Train & Test", [.5,.2]) 
  make_label("Enter test size (0< n <1)", [.5,.3],16) 

  entry = customtkinter.CTkEntry(master=app, 
                                 width=200, 
                                 height=25, 
                                 corner_radius=10) 
  entry.place(relx=.5, rely=.4, anchor=tkinter.CENTER) 

  def get_input():
    """validate the input then call the train function"""
    #input is the test size
    input = entry.get()
    if is_float_in_range(input) == False:
      tkinter.messagebox.showerror("Test size Error","INVALID TEST SIZE, Please enter a Value between 0 and 1 !! ")
      return

    if   alg=="s": #svm
      algorithms.SVM(kernel,float(input)); 
    elif alg=="t": #dession tree
      algorithms.dession_tree(max_depth,float(input))
    elif alg=="k": #knn
      algorithms.KNN(n_neighbors,float(input))
    elif alg=="lr": #logistic regression
      algorithms.linear_regression(float(input))
  

  make_button("Train", get_input, [.5,.5]) 
  make_button("Test",algorithms.test, [.5,.6])
  make_button("show results", lambda: show_result_view(alg), [.5,.7])

  def back_func():
    """go back to the previous window -depending on the algorithm-"""
    del algorithms.model
    if   alg=="s":
      SVM_window()
    elif alg=="t":
      dession_tree_window()
    elif alg=="k":
      KNN_window()
    elif alg=="lr":
      select_algorithm()
  make_back_button(back_func)



def KNN_window():
  destroy_all(); 
  make_frame(); 
  make_label("KNN", [.5,.3]) 
  make_label("Enter number of neighbors", [.5,.4]) 
 
  entry = customtkinter.CTkEntry(master=app, 
                                width=200, 
                                height=25, 
                                corner_radius=10) 
  entry.place(relx=.5, rely=.5, anchor=tkinter.CENTER) 
 
  def submit(): 
    input = entry.get() 
    if input == "": 
      tkinter.messagebox.showerror("Features Error ","ENTER NUMBER OF FEATURES, PLEASE!! ") 
      return
    if input.isdigit() == False: 
      tkinter.messagebox.showerror("Features Error ","INVALID NUMBER OF FEATURES, PLEASE!! ") 
      return

    global n_neighbors
    n_neighbors = int(input)
    train_test_window("k")
 
  make_button("Submmit", submit, [.5,.7]) 
  make_back_button(select_algorithm) 

def dession_tree_window():
  destroy_all(); 
  make_frame(); 
  make_label("Dession Tree", [.5,.3]) 
  make_label("Enter max depth", [.5,.4]) 
 
  entry = customtkinter.CTkEntry(master=app,
                                width=200, 
                                height=25, 
                                corner_radius=10)
  entry.place(relx=.5, rely=.5, anchor=tkinter.CENTER) 
 
  def submit(): 
    input = entry.get()
    if input == "": 
      tkinter.messagebox.showerror("Features Error ","ENTER NUMBER OF FEATURES, PLEASE!! ") 
      return
    
    if input.isdigit() == False: 
      tkinter.messagebox.showerror("Features Error ","INVALID NUMBER !! ") 
      return
    global max_depth
    max_depth=int(input)
    train_test_window("t")

 
  make_button("Submmit", submit, [.5,.7]); 

  make_back_button(select_algorithm) 



def SVM_window():
  destroy_all(); 
  make_frame(); 
  make_label("SVM", [.5,.3]) 

  #function that assigns the selected choice to the global variable kernel 
  def kernelmenu_callback(choice): 
      global kernel
      kernel = choice

  def Submmit():
    if "kernel" not in globals():
      tkinter.messagebox.showerror("Kernel Error","PLEASE SELECT A KERNEL !! ")
      return
    train_test_window("s")

  make_option_menu(["linear", "rbf"], kernelmenu_callback, [.5,.4]) 
  make_button("Submmit", Submmit, [.5,.7]) 
  make_back_button(select_algorithm)
 


def select_algorithm(): 
  """Select algorithm window"""
  destroy_all()
  make_frame()
  make_label("Select Algorithm", [.5,.3])
  make_button("SVM",SVM_window, [.5,.4])
  make_button("Dession Tree",dession_tree_window, [.5,.5])
  make_button("KNN",KNN_window, [.5,.6])
  make_button("Linear Regression",lambda: train_test_window('lr'), [.5,.7])
  make_back_button(classification_window)
   
 
 
#classification window 
 
def classification_window():
  """Classification window"""
  destroy_all()
  make_frame()
  make_button("Load Dataset", load_dataset, [.5,.3])
  make_label("Enter feature number", [.5,.4]) 
 
  entry = customtkinter.CTkEntry(master=app, 
                                width=200, 
                                height=25, 
                                corner_radius=10)
  entry.place(relx=.5, rely=.5, anchor=tkinter.CENTER) 
 
  def submit(): 
    """validate inputs and go to the next window"""
    
    n_features = entry.get()
    #the entry.get() here is the number of features
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
    
    #if the number of features and the dataset are valid, then we can go to the next window
    select_algorithm()
 
  make_button("Submmit", submit, [.5,.7])
 
  make_back_button(main_window)
 
 
 
 
 
 
def main_window():
  """Main window"""
  destroy_all()
  make_frame() 
  make_label("machine learning project", [.5,.3]) 
  make_button("Classification", classification_window, [.5,.5]) 
 
 
    
main_window()


 
app.mainloop()

