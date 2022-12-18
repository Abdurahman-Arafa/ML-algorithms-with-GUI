import tkinter
import customtkinter
import algorithms

customtkinter.set_appearance_mode("dark");
customtkinter.set_default_color_theme("blue");

app = customtkinter.CTk()
app.geometry("400x500")

inpt=None;


# make a standard button
def make_button(st,fun,pos):
    
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
                                  bg_color="#ffdf76",
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

#----------------------------------------------------------------


def destroy_all():
  for w in app.winfo_children():
    w.destroy();


def load_dataset():
  print("load dataset ...")
  # algorithms.dataset=


#display algoritms windows

def select_algorithm():
  if algorithms.dataset is None:
    print("Upload dataset first !");
    #return 
  if False : #val is None
    print("enter feature number")
  
  if False : #val.is_integer()
    print("Invalid numbers !");
    #return

    
  destroy_all();
  make_frame();
  make_label("Select Algorithm", [.5,.3]);
  make_button("SVM",algorithms.SVM, [.5,.4]);
  make_button("Dession Tree",algorithms.dession_tree, [.5,.5]);
  make_button("KNN",algorithms.KNN, [.5,.6]);
  make_back_button(classification);
  


#classification window

def classification():

  destroy_all();
  make_frame();
  make_button("Load Dataset", load_dataset, [.5,.3]);
  make_label("Enter feature number", [.5,.4])
  make_input([.5,.5]);
  make_button("Submmit", select_algorithm, [.5,.7]);
  make_back_button(main_window);





def main_window():
  
  make_frame();
  make_label("machine learning project", [.5,.3])
  make_button("Classification", classification, [.5,.5]);


   
main_window();


app.mainloop()
