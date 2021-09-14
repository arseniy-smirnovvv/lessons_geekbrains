let deposit = 1000; // Это начальная ставка
let quit = true; // Это переменная отвечает за выход из игры.
let repeat_type_bid = true; // Отвечает за то, что бы был выбран тип игры
let repeat_color_bid = false; // Ответ за выбор цвета
let repeat_number_bid = false;
let type_bid;
let num_bid;
let color_bid;
let bid;

function getRandomArbitrary(min, max) {
   // случайное число от min до (max+1)
  let rand = min + Math.random() * (max + 1 - min);
  return Math.floor(rand);
}


// Функция которая выходит из игры, если находит в введенном строке слово "quit"
function exit_game(txt){
  if(txt == 'quot') {
    console.log('Вы вышли из игры');
    return true;
  }
  return false;
};


// Сам цикл игры
while (quit){
  let random_num = getRandomArbitrary(0, 36);
  let random_color = getRandomArbitrary(1, 2);

  if (deposit == 0) {
  	console.log('Баланс равен нулю!');
    break;
  }

  // Если до этого тип ставка была введена, а тип игры не был выбран, тогда ввод ставки пропускается
  if (repeat_type_bid){
    bid = prompt('Ваш баланс: ' +deposit + ' Ваша ставка:');
  	if (exit_game(bid)) break;

    bid = Number(bid);

    if(bid <= 0 || bid > deposit || bid == undefined || isNaN(bid)){
      repeat_type_bid = true;
      continue;
    }

    deposit = deposit - bid;
  }

  // Если ставка была введена, тип игры выбран, а цвет не выбирается, то действия по выбору цвету будут повторяться
  if (repeat_color_bid){
  	type_bid == 1;
  } else if (repeat_number_bid){
  	type_bid == 2;
  } else {
    type_bid = prompt('Выберите тип ставки. Где 1 - это ставка на цвет, а 2 - это ставка на число');
   if (exit_game(type_bid)) break;
  }


    //Если выбрана ставка на цвет
 	if(type_bid == 1){
      color_bid = prompt ('Выберите цвет: где 1 - это черный, а 2 - это красный.');
      if (exit_game(color_bid)) break;

      if(color_bid != 1 && color_bid != 2){
  		repeat_color_bid = true;
        repeat_type_bid = false;
        continue;
      }
    // Если выбрана ставка на число
    } else if (type_bid == 2){
      num_bid = prompt('Введите число от 0 до 36');
      if (exit_game(num_bid)) break;

      num_bid = Number(num_bid);

      if(isNaN(num_bid) || num_bid < 0 || num_bid > 36){
        repeat_type_bid = false;
        repeat_number_bid = true;
        continue;
      }
    } else {
      repeat_type_bid = false;
      continue;
    }


  	if (type_bid == 1){
      if(color_bid == random_color){
        deposit += bid*2;
        alert('Поздравляем! Вы выиграли ' +bid*2+ '. Ваш баланс составляет: ' + deposit);
      } else {
        alert ('К сожалению вы ничего не выиграли! Ваш баланс составляет: ' + deposit);
      }
    } else if (type_bid == 2){
      if (num_bid == random_num){
      	deposit += bid*35;
        alert('Поздравляем! Вы выиграли ' +bid*35+ '. Ваш баланс составляет: ' + deposit);
      } else {
        alert ('К сожалению вы ничего не выиграли! Ваш баланс составляет: ' + deposit);
      }
    }

   repeat_type_bid = true;
  	  repeat_color_bid = false;
  	  repeat_type_bid = true;
      repeat_number_bid = false;


}
