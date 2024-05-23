"use client"
import React, { useEffect, useState } from 'react';
import Registered_Navbar from '../components/Registered_Navbar';
import Link from 'next/link'
import axios from 'axios';

function ShopPage(){
    const [name, getName] = useState("");

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
                  form.reset();
                  localStorage.setItem('cakename',formattedName),
                  window.location.href = '/mainshop';
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
        </div>
    
    )
}

export default ShopPage