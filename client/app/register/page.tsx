"use client"
import React, {useState, useEffect, use} from 'react'
import Link from 'next/link'
import Navbar from '../components/Navbar'
import { stringify } from 'querystring';
import { ok } from 'assert';
import { NextResponse } from 'next/server';
import axios from 'axios';

function RegisterPage() {
    const [usrinfo, setUsrInfo] = useState([{}]);
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [error, setError] = useState("");

    // useEffect(() => {
    //   axios.get('http://localhost:8000/api/register')
    //   .then(res => {
    //     setUsrInfo(res.data)
    //   })
    // });

    // const addUsrInfoHandler = () => {
    //   axios.post('http://localhost:8000/api/register', {
    //     'name':name,
    //     'email':email,
    //     'password':password
    //   })
    //   .then(res => console.log(res))
    // }
    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) =>{
      e.preventDefault(); //prevent refresh
        try{
            if(!name || !email || !password || !confirmPassword){
              setError("Please fill out all the forms");
              return;
            }
            if (password != confirmPassword){
              setError("Password do not match!!");
              return;
            }
            const res = await axios.post("http://localhost:8000/api/users",{
              'name':name,
              'email':email,
              'password':password
            });
            if (res.status === 200){
                const form = e.target as HTMLFormElement;
                setError(""); //clear err
                form.reset();
            } else{
              console.log("User registration failed.");
            }
          }
          catch(error){
            console.log("Error during registration: ",error);
          }
    }
  return (
    <div>
      <Navbar />
      <div className ="container mx-auto py-5">
        <h3>Register Page</h3>
        <hr className=" my-3" />
        <form onSubmit={handleSubmit}>
            {
              error && (
                <div className='bg-red-500 w-fit text-sm text-white py-1 px-3 rounded-md mt-2'>
                  {error}
                </div>
              )
            }
            <input onChange={(e) => setName(e.target.value)} className="block bg-gray-300 p-2 my-2 rounded-md"type="email" placeholder="Enter your email" />
            <input onChange={(e) => setEmail(e.target.value)} className="block bg-gray-300 p-2 my-2 rounded-md"type="text" placeholder="Enter your name" />
            <input onChange={(e) => setPassword(e.target.value)} className="block bg-gray-300 p-2 my-2 rounded-md"type="password" placeholder="Enter your password" />
            <input onChange={(e) => setConfirmPassword(e.target.value)} className="block bg-gray-300 p-2 my-2 rounded-md"type="password" placeholder="Confirm your password" />
            <button type='submit' className='bg-green-500 p-2 text-gray-50 rounded-md'>Sign up</button>
        </form>
        <hr className='my-3' />
          <p>Already have an account? <Link className='text-blue-500 hover:underline' href="/login">Log-in</Link></p>
      </div>
    </div>
  )
}

export default RegisterPage
