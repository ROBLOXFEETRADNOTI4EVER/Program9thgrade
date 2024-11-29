function getInputValue() {
    const input = document.querySelector("#myInput").value;
    console.log(input); 
}



// async function getData() {
//     const url = " http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={e19c42b615d07843c4780e7fc0987adf}";
//     try {
//       const response = await fetch(url);
//       if (!response.ok) {
//         throw new Error(`Response status: ${response.status}`);
//       }
  
//       const json = await response.json();
//       console.log(json);
//     } catch (error) {
//       console.error(error.message);
//     }
//   }
// //   e19c42b615d07843c4780e7fc0987adf

// const prices = [5,30,10,25,15,20];
// const total = prices.reduce(sum);
// // console.log(total);
// // it bassicly makes so all of the values in the array get added or summed together this feture is pretty usefull

// console.log(`$${total.toFixed(2)}`);
// // we use tofixed to get the 2 decimals its fucking good and good feture must use in the future
// function  sum(accumulator,element){
//     return accumulator + element;
// }

// ------------------------------------------------------------------------------------------|
// const grades = [4,3,2,4,5,3,2,4,1,2,3,2,1,3,4,5,5,2,4,3,2,4,2,2,1,3,1,3,5,6,2,1,4,5];     |
// const avragGrades = grades.reduce(Avrage);                                                |
// console.log(`${avragGrades.toFixed(2)}`);                                                 |
//                                                                                           |
// function Avrage(accumulator,element){                                                     |
//     return (accumulator + element) / element;                                             |
// }                                                                                         |
// ------------------------------------------------------------------------------------------|

