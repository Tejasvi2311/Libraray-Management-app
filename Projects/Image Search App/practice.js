//1.Ways to print in Javascript

// console.log("Hello World");
//alert("text");
document.write("this is document write");

//2.Javascript console API

console.log("Hello World",4+6,"Another log");
console.warn("This is a warning");
console.error("This is a error");

//3.Javascript Variables

var num1=34;
var num2=56;
console.log(num1+num2);

//4.Data Types in JavaScript

//Numbers
var num1=34;
var num2=56;

//Strings
var str1="This is a string";
var str2='This is also a string';

//Objects
var marks={
    ravi: 34,
    shubham: 78,
    harry: 99
}

console.log(marks)

//booleans

var a=true;
var b=false;

var und=undefined;  // a variable is not initialised and only declared it is undefined by default
console.log(und);

var n=null;
console.log(n);

/*There are 2 types of data types in Javascript
1.Primitive Data type: undefined,null,number,string,boolean,symbol
2.Reference Data Type: Arrays,Objects */

var arr=[1,2,3,4,5];  //mix data types possible
console.log(arr);

//5.Functions in Javascript

function add(a,b){
    return a+b;
}

c=add(3,4);
d=add(5,6);

console.log(c,d);

//6. Conditional Statements

    //1. Single if
    //2. if...else
    //3.if...else if...else

//7. LOOPS in Javascript
    var arr = [1, 2, 3, 4, 5, 6, 7];
    console.log(arr);
    // for(var i=0;i<arr.length;i++){
    //     if(i==2){
    //         //break;
    //         continue;
           
    //     }
    //     console.log(arr[i])
    // }
    
    // arr.forEach(function(element)
    // {console.log(element);

    // })  // same as above for loop

    // const ac = 0; // const variable can only be declared and not assigned, used when a variable is never going to be updated
    // ac++; //throw error being const
    // ac = ac +1; //throw error being const
    let j = 10;  // let variable scope is a block level scope for a variable(inside curly braces)
    // while(j<arr.length){
    //     console.log(arr[j]);
    //     j ++;
    // }
    
    do{
        console.log("Me toh bolunga!")
        console.log(arr[j]);  // must executing statement even if condition is false
        j++;
    } while (j < arr.length);
    
    //7.Array Methods

    let myArr = ["Fan", "Camera", 34, null, true];
    console.log(myArr.length);
    // myArr.pop();
    // console.log(myArr);
    // myArr.push("harry")
    // console.log(myArr);
    // myArr.shift() //removes first element of array
    // console.log(myArr);
    const newLen = myArr.unshift("Harry")  //to add new element as first element of array| this statement will specifically give length as well
    // console.log(newLen);
    //myArr.toString();
    //myArr.sort();  
    //console.log(myArr);
    
    //8. String Methods in JavaScript
    let myLovelyString = "Harry is a good boy good good Harry";
    // console.log(myLovelyString.length)
    //  console.log(myLovelyString.indexOf("good"))
    //  console.log(myLovelyString.lastIndexOf("good"))
    // console.log(myLovelyString.slice(1,4))   //1-->(4-1)

    d = myLovelyString.replace("Harry", "Rohan");
    // d = d.replace("good", "bad");
    // console.log(d, myLovelyString)  // replace methods replace only first occurence
    
    let myDate = new Date();
    console.log(myDate.getTime());
    console.log(myDate.getFullYear());
    console.log(myDate.getDay());  //sun-->sat|0-->6
    console.log(myDate.getMinutes());
    console.log(myDate.getHours());
     
    //9. DOM Manipulation (Document Object Model) 
    // A webpage,html code is a DOM which gives manipulation techniques to make changes in HTML page on browser or outside browser

    let elem = document.getElementById('click');
    console.log(elem);
    
    let elemClass = document.getElementsByClassName("container")
    console.log(elemClass);

    //elemClass[1].style.background = "pink";
    elemClass[0].classList.add("bg-primary")   //added/used class bg-primary for 1st container class
    elemClass[0].classList.add("text-success")
    //elemClass[0].classList.remove("text-success") // to remove added class in a class container

    // console.log(elem.innerHTML);
    // console.log(elem.innerText); 
    
    // console.log(elemClass[0].innerHTML);
    // console.log(elemClass[0].innerText); 

    // tn = document.getElementsByTagName('div')
    // console.log(tn)

    // createdElement = document.createElement('p');
    // createdElement.innerText = "This is a created para";
    // tn[0].appendChild(createdElement);

    // createdElement2 = document.createElement('b');
    // createdElement2.innerText = "This is a created bold";

    // tn[0].replaceChild(createdElement2, createdElement);

    //removeChild(element); //---> removes an element
     
    // Selecting using Query
    // sel = document.querySelector('.container')
    // console.log(sel)
    // sel = document.querySelectorAll('.container')
    // console.log(sel)
    
    function clicked(){    // function for click button
        console.log('The button was clicked')
    }
    window.onload = function(){
        console.log('The document was loaded')
    
    }
    //10.Events in JavaScript


    // firstContainer.addEventListener('click', function(){
    //     document.querySelectorAll('.container')[1].innerHTML = "<b> We have clicked</b>"
    //     console.log("Clicked on Container")
    // })
    
    // firstContainer.addEventListener('mouseover', function(){
    //     console.log("Mouse on Container")
    // })
    
    // firstContainer.addEventListener('mouseout', function(){
    //     console.log("Mouse out of Container");
    // })
    
    // let prevHTML = document.querySelectorAll('.container')[1].innerHTML;

    // firstContainer.addEventListener('mouseup', function(){
    //     document.querySelectorAll('.container')[1].innerHTML = prevHTML;
    //     console.log("Mouse up when clicked on Container");
    // })
    
    // firstContainer.addEventListener('mousedown', function(){
    //     document.querySelectorAll('.container')[1].innerHTML = "<b> We have clicked</b>"
    //     console.log("Mouse down when clicked on Container");
    // })
    
    
    // Arrow Functions

    // function summ(a, b){
    //     return a+b;
    // }
    summ = (a,b)=>{
        return a+b;
    }
    
    logKaro = ()=>{
        document.querySelectorAll('.container')[1].innerHTML = "<b> Set interval fired</b>"
        console.log("I am your log")
    }
    //11. SetTimeout and setinterval

    // clr = setTimeout(logKaro, 2000);
    // clr = setInterval(logKaro, 2000);
    // use clearInterval(clr)/clearTimeout(clr) to cancel setInterval/setTimeout
    
    //12. JavaScript localStorage
    // localStorage.setItem('name', 'harry') 
    // localStorage 
    // localStorage.getItem('name')
    // localStorage.removeItem('name')
    // localStorage.clear();
    
    //13. Json 
    obj = {name: "harry", length: 1, a: {this: 'tha"t'}}
    jso = JSON.stringify(obj);
    console.log(typeof jso)
    console.log(jso)
    // parsed = JSON.parse(`{"name":"harry","length":1,"a":{"this":"that"}}`)
    // console.log(parsed);
    
    // Template literals - Backticks
    
    a = 34;
    console.log(`this is my ${a}`)