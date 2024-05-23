import Link from 'next/link';
import React, { useEffect, useState } from 'react';
import { useRouter } from 'next/router';

function Registered_Navbar() {
  const [name, setName] = useState('');

  useEffect(() => {
    if (typeof window !== 'undefined') {
      const storedName = localStorage.getItem('name');
      if (storedName) {
        setName(storedName);
      }
    }
  }, []);

  return (
    <nav className="bg-[#333] text-white p-2 w-full">
      <div className="container mx-auto">
        <div className="flex justify-between items-center">
          <div>
            <Link href="/">Home</Link>
          </div>
          <ul className="flex">
            <li className="mx-3">Welcome, {name}</li>
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Registered_Navbar;
