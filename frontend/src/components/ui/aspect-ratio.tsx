"use client";

import * as AspectRatioPrimitive from "@radix-ui/react-aspect-ratio@1.1.2";
import { apiService } from '../services/api';


function AspectRatio({
  ...props
}: React.ComponentProps<typeof AspectRatioPrimitive.Root>) {
  return <AspectRatioPrimitive.Root data-slot="aspect-ratio" {...props} />;
}

export { AspectRatio };
