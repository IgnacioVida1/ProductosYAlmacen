package com.example.logistica.controller;

import com.example.logistica.entity.Vehiculo;
import com.example.logistica.service.VehiculoService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
public class VehiculoController {

    private final VehiculoService vehiculoService;

    public VehiculoController(VehiculoService vehiculoService) {
        this.vehiculoService = vehiculoService;
    }

    @PostMapping("/vehiculos")
    public ResponseEntity<Vehiculo> registrarVehiculo(@RequestBody Vehiculo v){
        return ResponseEntity.ok(vehiculoService.registrarVehiculo(v));
    }

    @GetMapping("/vehiculos/{id}")
    public ResponseEntity<Vehiculo> consultarVehiculo(@PathVariable Long id){
        return ResponseEntity.ok(vehiculoService.consultarVehiculo(id));
    }

    @PutMapping("/vehiculos/{id}/asignarConductor/{idConductor}")
    public ResponseEntity<Vehiculo> asignarConductorAVehiculo(@PathVariable Long id, @PathVariable Long idConductor){
        return ResponseEntity.ok(vehiculoService.asignarConductorAvehiculo(id, idConductor));
    }
}
