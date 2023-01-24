import { AxiosResponse } from 'axios';
import type { NextApiRequest, NextApiResponse } from 'next'
const axios = require('axios');

type ResponseData = {
  numeral ?: string
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
    let response = await axios.get(process.env["BACKEND_URL"] + "/number-to-numeral?number=" + req.query.number)
    if (response.data.numeral) {
      res.status(200).json({numeral: response.data.numeral})
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
