"use client"
import React, { useEffect, useState } from 'react';
import Registered_Navbar from '../components/Registered_Navbar';
import Link from 'next/link'
import axios from 'axios';

function ThankYouPage(){
    const [name, getName] = useState("");

    return(
        <div>
            <Registered_Navbar />
            <div className="flex justify-center items-center mt-4 bg-cover bg-center">
                <h1>Thank You For Your Purchase, Your order has been placed</h1>
            </div>
            <div className="flex justify-center items-center mt-4 bg-cover bg-center">
                <Link className='text-blue-500 hover:underline' href={"/search"}>Continue Shopping</Link>
            </div>
        </div>
    
    )
}

export default ThankYouPage