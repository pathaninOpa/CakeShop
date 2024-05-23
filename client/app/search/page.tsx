"use client"
import React, {useEffect, useState} from 'react'
import Registered_Navbar from '../components/Registered_Navbar';
import Link from 'next/link'
import axios from 'axios';

function ShopPage(){
    const [usrname, setUsrName] = useState("");
    const [name, getName] = useState("");
    const [cakeData, setCakeData] = useState(null);
    
    useEffect(() => {
      if (typeof window !== 'undefined') {
        const storedName = localStorage.getItem('name');
        if (storedName) {
          setUsrName(storedName);
        }
      }
    }, []);

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
                  // localStorage.setItem('cakename',cakeData),
                  // window.location.href = '/mainshop';
              } else{
                console.log("Cake search api failed.");
              }
            }
            catch(error){
              console.log("Error during search",error);
            }
            }

            const handleClick = async () =>{
                try{
                    const res = await axios.post(`http://localhost:8000/api/orders`,{
                        "name":(cakeData as any).name,
                        "UserName": usrname
                    });
                    if (res.status === 200){
                        // localStorage.setItem('cakename',cakeData),
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
            <div className="flex justify-center items-center mt-4 bg-cover bg-center">
              <form onSubmit={handleSubmit}>
                <div className="flex items-center space-x-2">
                  <input onChange={(e) => getName(e.target.value)} className="bg-gray-300 p-2 rounded-md" type="text" placeholder="Type Cake name"/>
                  <button type="submit" className="bg-blue-400 p-2 text-gray-50 rounded-md">Search</button>
                </div>
              </form>
            </div>
            {/* Render cake data */}
            {cakeData && (
      <div className="flex justify-center">
        <div className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
          <h2 className="text-xl font-semibold mb-2 ">Cake Details</h2>
          <img className="w-full mb-2 max-w-xs" src={(cakeData as any).image} alt={(cakeData as any).name} />
        </div>
        <div className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
          <p className="text-gray-700 mb-2"><span className="font-bold">Name: </span> {(cakeData as any).name}</p>
          <p className="text-gray-700 mb-2"><span className="font-bold">Short Description: </span>{(cakeData as any).shortDescription}</p>
          <p className="text-gray-700 mb-2"><span className="font-bold">Description: </span>{(cakeData as any).description}</p>
          <p className="text-gray-700 mb-2"><span className="font-bold">Ingredients: </span>{(cakeData as any).ingredients}</p>
          <p className="text-gray-700 mb-2"><span className="font-bold">Recipe: </span>{(cakeData as any).recipe}</p>
          <p className="text-gray-700 mb-2"><span className="font-bold">Stock: </span>{(cakeData as any).stock}</p>
        </div>
      </div>
      
    )}
    <div className="flex justify-center items-center mt-4 bg-cover bg-center">
      <div className="flex items-center space-x-2">
        <button type="submit" className="bg-green-500 px-4 py-2 text-gray-50 rounded-md" onClick={handleClick}>Buy</button>
      </div>
    </div>
        </div>
    )
}

export default ShopPage