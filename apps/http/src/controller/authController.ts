import { Request, Response } from "express";
import {prisma} from "@repo/db"
import bcrypt from "bcrypt";
export const signup=async(req:Request,res:Response)=>{
    const {
        username,
        email,
        password
    }=req.body;
    try{
        const existingUser=await prisma.user.findUnique({
            where:{
                email
            }
        }) 
        if(existingUser){
            return res.status(400).json({error:"User already exists"});
        }
        const hashedPassword=await bcrypt.hash(password,10);
        const user=await prisma.user.create({
            data:{
                username,
                email,
                password:hashedPassword
            }
        })
        res.status(201).json({message:"User created successfully"});

    }catch(e){
        console.log(e);
        res.status(500).json({error:"Internal Server Error"});
    }
}