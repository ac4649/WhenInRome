import Head from 'next/head'
import Image from 'next/image'
import { Inter } from '@next/font/google'
import styles from '@/styles/Home.module.css'
import { Box, Form, Text } from 'grommet'
import { Grommet } from 'grommet'
import RomanToNumberForm from '@/components/RomanToNumberForm'
import NumberToRomanForm from '@/components/NumberToRomanForm'
import RomanAdditionForm from '@/components/RomanAdditionForm'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  return (
    <>
      <Head>
        <title>Roman Numeral Conversion App</title>
        <meta name="description" content="Convert Roman Numerals to Numbers and vice-versa" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className={styles.main}>
        <Box gap="small" fill align="center">
          <Box direction="row-responsive" gap="small" fill>
            <RomanToNumberForm
              formTitle = "Convert from Roman Numerals to Numbers"
              formBoxProps={{
                pad: "small",
                background: "white",
                gap: "xsmall",
                border: "all",
                fill: true
              }}
            />
            <NumberToRomanForm
              formTitle = "Convert from Number to Roman Numerals"
              formBoxProps={{
                pad: "small",
                background: "white",
                gap: "xsmall",
                border: "all",
                fill: true
              }}
            />
          </Box>
          <Box direction="row" fill  align="center">
            <RomanAdditionForm
              formTitle = "Add Roman Numerals"
              formBoxProps={{
                pad: "small",
                background: "white",
                gap: "xsmall",
                border: "all",
                fill: true
              }}
            />
          </Box>
        </Box>
      </main>
    </>
  )
}
