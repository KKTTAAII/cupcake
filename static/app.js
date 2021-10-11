$ul = $(".cupcakes");
$submitBtn = $(".btn");

const BASE_URL = "http://127.0.0.1:5000/api";

getAllCupcakes()

function generateCupcakeHTML(cupcake){
    return `
    <div data-id=${cupcake.id}>
    <li>${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
    <button class="delete-button">X</button>
    </li> 
    <img src="${cupcake.image}" class="cupcakeImage">`
}

async function getAllCupcakes() {
  let response = await axios.get(`${BASE_URL}/cupcakes`);
  allCupcakes = response.data.cupcakes; //list
  for(i=0; i<allCupcakes.length; i++){
      cupcake = allCupcakes[i];
      $ul.append(generateCupcakeHTML(cupcake));
  }
}

$submitBtn.click( async function(e){
    e.preventDefault();
    const data = {
        flavor: $("#flavor").val(),
        size: $("input[type='radio'][name='size']:checked").val(),
        rating: $("#rating").val(),
        image: $("#image").val()
    };
    let response = await axios.post(`${BASE_URL}/cupcakes`, json=data);
    let newCupcake = generateCupcakeHTML(response.data.cupcake);
    console.log(response.data.cupcake.image)
    $ul.append(newCupcake);
    $("form").trigger("reset");
})

$(".cupcakes").on("click", ".delete-button", async function (evt) {
    evt.preventDefault();
    let $cupcake = $(evt.target).closest("div");
    let cupcakeId = $cupcake.attr("data-id");
    await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
    $cupcake.remove();
})
