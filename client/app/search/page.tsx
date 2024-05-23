"use client"
import React, {useState} from 'react'
import Registered_Navbar from '../components/Registered_Navbar';
import Link from 'next/link'
import axios from 'axios';

function ShopPage(){
    const [name, getName] = useState("");
    const [cakeData, setCakeData] = useState(null);

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) =>{
        e.preventDefault(); //prevent refresh
          try{
              const formattedName = name.replace('+', '%20');
              const res = await axios.get(`http://localhost:8000/api/cakes`,{
                params:{
                  'name':formattedName
                }
              });
              if (res.status === 200){
                  const form = e.target as HTMLFormElement;
                  setCakeData(res.data);
                  form.reset();
                  // localStorage.setItem('cakename',formattedName),
                  // window.location.href = '/mainshop';
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
              <input onChange={(e) => getName(e.target.value)} className="block bg-gray-300 p-2 my-2 rounded-md"type="text" placeholder="Type Cake name" />
              <button type='submit' className='bg-blue-400 p-2 text-gray-50 rounded-md'>Search</button>
              </form>
            </div>
            {/* Render cake data */}
            {cakeData && (
                <div className="flex justify-center">
                    <h2>Cake Details</h2>
                    <p>Name: {(cakeData as any).name}</p>
                    <p>Short Description: {(cakeData as any).shortDescription}</p>
                    <p>Description: {(cakeData as any).description}</p>
                    <p>Image: {(cakeData as any).image}</p>
                    <p>Ingredients: {(cakeData as any).ingredients}</p>
                    <p>Recipe: {(cakeData as any).recipe}</p>
                    <p>Stock: {(cakeData as any).stock}</p>
                    {/* Render other cake data properties as needed */}
                </div>
            )}
        </div>
    
    )
}

export default ShopPage