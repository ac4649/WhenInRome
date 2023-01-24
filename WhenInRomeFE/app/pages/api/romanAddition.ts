import { AxiosError, AxiosResponse } from 'axios';
import type { NextApiRequest, NextApiResponse } from 'next'
const axios = require('axios');

type ResponseData = {
    sum ?: string
  error ?: string
}

export const config = {
  api: {
    responseLimit: false,
  },
};

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<ResponseData>
) {

  try {
    let response = await axios.get(process.env["BACKEND_URL"] + "/roman_addition?numeral1=" + req.query.numeral1 + "&numeral2=" + req.query.numeral2)
    if (response.data.sum) {
      res.status(200).json({sum: response.data.sum})
    } else {

      if (response.status == 200) {
        res.status(200).json({error: response.data.error})
      } else {
        res.status(200).json({error: "An Unknown Error Occured"})
      }
      
    }
  
  } catch (error) {
    res.status(200).json({error: "An Unknown error occured"})
  }
  
}
