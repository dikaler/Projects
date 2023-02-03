//To Do List JS
let input = document.getElementById("inputText");
let list= document.getElementById("list");
let minimalValue = 0;
let listNum = 0;
addList=()=>{
    //Get user task
    let inputText = filterList(input.value);
    //Once there is a user entered task, create row as well as edit, delete buttons.
   if (inputText) {
    list.innerHTML += ` <li class=" my-3 py-3 shadow list-group-item " id="list${listNum}">
                <div class="row">
                <div class="col-1">
                <input class="" type="checkbox" id="check${listNum}" onclick="done(${listNum})">
                </div>
                <div class="col-6">
                    <span class=" h4" id="text${listNum}"> ${inputText} </span>
                </div>
                <div class="col-4">
                     <button onclick="deleteList(${listNum})"><i class="fa-solid fa-trash fa-xl"></i></button>
                     <button onclick="editList(${listNum})"><i class="fa-solid fa-pen-to-square fa-xl"></i></button>
                </div>                  
                 </div>    
                </li> `;
        input.value="";
        listNum++;

   }
}

//Allow user to check off items.
done=(listId)=>{ 
    //get task id
    let checkbox = document.getElementById(`check${listId}`);
    //current state of task
    let current = document.getElementById(`text${listId}`);
    //line through symbolizes task done
    let classExit=current.classList.contains("text-decoration-line-through");
    //If task is not marked done, no line through
    if (classExit == true) {
        current.classList.remove("text-decoration-line-through");
    //Put line through task, if completed
    }else{
        current.classList.add("text-decoration-line-through");
    }
    
}

//Make sure user inputs valid task, needs to be atleast one character.
filterList=(x)=>{
       if (x) {
            if (x.length >= minimalValue) {
                return x;
            }
       }
       else{
            alert("Please enter atleast one character.");
       }
}

//Edit Task
editList=(listId)=>{
    //get task id
    let currentText = document.getElementById(`text${listId}`);
    //get user's updated title
    let newText = prompt("Change the title of your task below.",currentText.innerHTML);
    //once you click finish, the task is updated (whether there is a change or not)
    if (filterList(newText)) {
        currentText.innerHTML = newText; 
        alert("Your task has been successfully edited.");
    }
    else{
        alert("No change was made.");
    }
};

//Delete from List
deleteList=(listId)=>{
    //get task id
    let current = document.getElementById(`text${listId}`).innerHTML;
        //confirm with user if they'd like to delete
       let deleteComfirm = confirm(`Are you sure you want to delete "${current}"?`);
    if (deleteComfirm) {
         let p = document.getElementById("list")
        let c = document.getElementById(`list${listId}`);
        p.removeChild(c);
        alert("Your task has been deleted.");
    }
    //
    else{
        alert("Deletion cancelled.");
    }
};