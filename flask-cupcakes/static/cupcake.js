const BASE_URL = "http://localhost:5000/api"

function makeCupcakeHOME(cupcake) {
    return `
    <div class=""data-cupcake-id=${cupcake.id}>
      <li class="list-group-item text-center">
        ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
        <button class="delete-button btn-sm btn-danger">X</button>
      </li>
      <img class="Cupcake-img img-fluid rounded mx-auto d-block"
            src="${cupcake.image}"
            alt="(no image provided)">
    </div>
   `;
}

async function showCupcakes() {
    const response = await axios.get(`${BASE_URL}/cupcakes`);
    
    console.log(response)

    for (let cupcakedata of response.data.cupcakes) {
        let newCake = $(makeCupcakeHOME(cupcakedata));
        $("#cupcakes-list").append(newCake);
    }
}

$("#new-cupcake-form").on("submit", async function (evt){
    evt.preventDefault();

    let flavor = $("#form-flavor").val();
    let rating = $("#form-rating").val();
    let size = $("#form-size").val();
    let image = $("#form-image").val();

    const newCakeResponse = await axios.post(`${BASE_URL}/cupcakes`, 
    {flavor,rating,size,image})

    let newCupCake = $(makeCupcakeHOME(newCakeResponse.data.cupcake));
    $("#cupcakes-list").append(newCupCake);
    $("#new-cupcake-form").trigger("reset");

});

$("#cupcakes-list").on("click", ".delete-button", async function (evt) {
    evt.preventDefault();
    let $cupcake = $(evt.target).closest("div");
    let cupcakeId = $cupcake.attr("data-cupcake-id");
  
    await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
    $cupcake.remove();
  });
  
  
  $(showCupcakes);
  