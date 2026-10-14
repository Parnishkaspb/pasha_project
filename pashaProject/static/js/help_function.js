// функция NewQuery предназчанена для получения данных без перезагрузки! 
// Нужно чтобы города, ключевые слова выпадали списком
function NewQuery(List, htmlName, whereQuery, inputvalue, pathToImage, whatList){
    const query = inputvalue.value.trim();
    if (query === '') {
        List.innerHTML = '';
        return;
    }

    fetch(`/`+whereQuery+`/?query=${query}`)
        .then(response => response.json())
        .then(lists => {
            // console.log(lists) 
            List.innerHTML = '';
            lists.forEach(item => {
                let word = query.substr(0, query.length) + " ";
                word += item.title.substr(query.length);

                CreateList(List, htmlName, word, whatList, item.title, pathToImage)
            });
        });
}

function doSomething(whereAddTitle, title, addOrDelete){
    // 1 --> Список городов city-input, city-input-hidden, city-list-add, city-list-delete
    // 2 --> Чем занимается человек
    // 3 --> Ключевые слова
    if (whereAddTitle == 1){
        const input = document.getElementById('city_input_hidden');
        const cityListAdd = document.getElementById('city_list_delete');
        cityListAdd.innerHTML = '';
        FordoSomething(addOrDelete, input, title, whereAddTitle, cityListAdd, 'city')
    }
    if (whereAddTitle == 2){
        const input = document.getElementById('whatdo_input_hidden');
        const whatdoListAdd = document.getElementById('whatdo_list_delete');
        whatdoListAdd.innerHTML = '';
        FordoSomething(addOrDelete, input, title, whereAddTitle, whatdoListAdd, 'whatdo')
    }
    if (whereAddTitle == 3){
        const input = document.getElementById('keyword_input_hidden');
        const keywordListAdd = document.getElementById('keyword_list_delete');
        keywordListAdd.innerHTML = '';
        FordoSomething(addOrDelete, input, title, whereAddTitle, keywordListAdd, 'keyword')
    }
}

function FordoSomething(addOrDelete, input_hidden, title, whereAddTitle, List, where){
    let emptyMassive = [];
    if (addOrDelete == 1){
        const deleteValue = document.getElementById(where+'_input');
        deleteValue.value = '';
        if (input_hidden.value.length != 0){
            emptyMassive = input_hidden.value.split(',');
        }
        if (!input_hidden.value.includes(title)){
            emptyMassive.push(title);
            input_hidden.value = emptyMassive;
            emptyMassive.forEach(word => {
                CreateList(List, where, word, whereAddTitle)
            });
        } else {
            emptyMassive = input_hidden.value.split(',');;
            emptyMassive.forEach(word => {
                CreateList(List, where, word, whereAddTitle)
            });
        }
    } else {
        emptyMassive = input_hidden.value.split(',');
        emptyMassive.splice(emptyMassive.indexOf(title), 1);
        input_hidden.value = emptyMassive;
        emptyMassive.forEach(word => {
            CreateList(List, where, word, whereAddTitle)
        });
    }
}

function CreateList(List, htmlName, word, whatList, empty='', pathToImage='static/images/free-icon-close-6276642.png'){
    const listItem = document.createElement('li');

    listItem.classList.add(htmlName+'_item');
        
    listItem.style.cursor = "pointer";
    const Name = document.createElement('span');

    Name.textContent = word;
        
    Name.classList.add(htmlName+'_name');

    const addIcon = document.createElement('img');
    addIcon.src = pathToImage;

    addIcon.classList.add('add_icon');
    

                    
    listItem.appendChild(Name);
    listItem.appendChild(addIcon);
    if (empty.length != 0){
        listItem.setAttribute("onclick", "doSomething("+whatList+",'"+ empty +"', 1)");
    } else {
        listItem.setAttribute("onclick", "doSomething("+whatList+",'"+ word +"', 2)");
    }
    // console.log(word);
    List.appendChild(listItem);
}