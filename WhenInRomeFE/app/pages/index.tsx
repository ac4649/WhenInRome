import Head from 'next/head'
import Image from 'next/image'
import { Inter } from '@next/font/google'
import styles from '@/styles/Home.module.css'
import { Box, Form, Text } from 'grommet'
import { Grommet } from 'grommet'
import RomanToNumberForm from '@/components/RomanToNumberForm'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  return (
    <Grommet full>
      <Head>
        <title>Roman Numeral Conversion App</title>
        <meta name="description" content="Convert Roman Numerals to Numbers and vice-versa" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className={styles.main}>
        <Box direction="row-responsive" gap="small">
          <RomanToNumberForm
              formTitle = "Convert from Roman Numerals to Numbers:"
              formBoxProps={{
                pad: "small",
                background: "white",
                gap: "xsmall"
              }}
            />
          <Box background="grey" pad="small">
            <Text>
              Convert from Numbers to Roman Numerals:
            </Text>
            <hr/>
            <>
              conversion box comes here
            </>
          </Box>
        </Box>
      </main>
    </Grommet>
  )
}
