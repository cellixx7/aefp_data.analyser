"use client";

import { useEffect, useState } from "react";

import { api } from "@/services/api";

type Country = {
  id: number;
  name: string;
  iso3: string;
};

export default function Home() {
  const [countries, setCountries] =
    useState<Country[]>([]);

  useEffect(() => {
    api.get("/countries/")
      .then((response) => {
        setCountries(response.data);
      });
  }, []);

  return (
    <main className="p-8">
      <h1 className="text-3xl font-bold">
        Portal AEFP
      </h1>

      <ul className="mt-4">
        {countries.map((country) => (
          <li key={country.id}>
            {country.name} ({country.iso3})
          </li>
        ))}
      </ul>
    </main>
  );
}
