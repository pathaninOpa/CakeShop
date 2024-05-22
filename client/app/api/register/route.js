// import {NextResponse} from "next/server"

// export async function POST(req){
//     try{
//         const{name, email, password} = await req.json();
//         console.log(name);
//         console.log(email);
//         console.log(password);
//         return NextResponse.json({Message: "User Registered"},{status: 201});
//     }
//     catch(e){
//         return NextResponse.json({Message: "Error Occured While Registering"}, {status: 500});
//     }
// }