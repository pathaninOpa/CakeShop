"use client"
import React, {useState} from 'react'
import Registered_Navbar from '../components/Registered_Navbar';
import Link from 'next/link'
import axios from 'axios';

function ShopPage(){
    const [name, setName] = useState("");
    const [shortDescription, setShortDescription] = useState("");
    const [description, setDescription] = useState("");
    const [image, setImage] = useState("");
    const [ingredients, setIngredients] = useState("");
    const [recipe, setRecipe] = useState("");
    const [stock, setStock] = useState("");

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) =>{
        e.preventDefault(); //prevent refresh
          try{
              const ingredientsList = ingredients.split(',').map(item => item.trim());
              const stockInt = parseInt(stock);

              const res = await axios.post(`http://localhost:8000/api/cakes`,{
                params:{
                  "name":name,
                  "shortDescription":shortDescription,
                  "description":description,
                  "image":image,
                  "ingredients":ingredientsList,
                  "recipe":recipe,
                  "stock":stockInt
                }
              });
              if (res.status === 200){
                  const form = e.target as HTMLFormElement;
                  form.reset();
              } else{
                console.log("Cake search api failed.");
              }
            }
            catch(error){
              console.log("Error during search",error);
            }
            }
    return(
        <div>
            <Registered_Navbar />
            <div className="flex justify-center items-center min-h-screen bg-cover bg-center">
              <form onSubmit={handleSubmit}>
              <input onChange={(e) => setName(e.target.value)} className="block bg-gray-300 p-2 my-2 rounded-md"type="name" placeholder="Type Cake name" />
              <input onChange={(e) => setShortDescription(e.target.value)} className="block bg-gray-300 p-2 my-2 rounded-md"type="text" placeholder="Enter ShortDescription" />
            <input onChange={(e) => setDescription(e.target.value)} className="block bg-gray-300 p-2 my-2 rounded-md"type="text" placeholder="Enter Cake Description" />
            <input onChange={(e) => setImage(e.target.value)} className="block bg-gray-300 p-2 my-2 rounded-md"type="text" placeholder="Enter Cake Image" />
            <input onChange={(e) => setIngredients(e.target.value)} className="block bg-gray-300 p-2 my-2 rounded-md"type="text" placeholder="Enter Cake Ingredients" />
            <input onChange={(e) => setRecipe(e.target.value)} className="block bg-gray-300 p-2 my-2 rounded-md"type="text" placeholder="Enter Cake Recipe" />
            <input onChange={(e) => setStock(e.target.value)} className="block bg-gray-300 p-2 my-2 rounded-md"type="number" placeholder="Enter Cake stock" />
              <button type='submit' className='bg-blue-400 p-2 text-gray-50 rounded-md'>Search</button>
              </form>
            </div>
        </div>
    
    )
}

export default ShopPage